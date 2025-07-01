from flask import Flask, request, render_template, send_file, jsonify, flash, redirect, url_for
import os
import tempfile
import zipfile
from pathlib import Path
from moviepy.editor import VideoFileClip
import time
import threading
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = 'webm_converter_secret_key_2025'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size

# Configuración
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'converted'
ALLOWED_EXTENSIONS = {'webm'}

# Crear carpetas si no existen
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Estado global para conversiones
conversion_status = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_video(file_id, input_path, output_path, quality='medium'):
    """Convierte un video WEBM a MP4"""
    try:
        conversion_status[file_id]['status'] = 'converting'
        conversion_status[file_id]['progress'] = 0
        
        # Configuración de calidad
        quality_settings = {
            'low': {'bitrate': '500k', 'desc': 'Baja Calidad'},
            'medium': {'bitrate': '1000k', 'desc': 'Calidad Media'},
            'high': {'bitrate': '2000k', 'desc': 'Alta Calidad'}
        }
        
        settings = quality_settings.get(quality, quality_settings['medium'])
        
        conversion_status[file_id]['message'] = f"Iniciando conversión con {settings['desc']}..."
        
        start_time = time.time()
        
        # Cargar y convertir video
        with VideoFileClip(input_path) as video:
            duration = video.duration
            conversion_status[file_id]['duration'] = f"{duration:.1f}s"
            conversion_status[file_id]['progress'] = 25
            
            conversion_status[file_id]['message'] = "Procesando video..."
            
            # Escribir archivo MP4
            video.write_videofile(
                output_path,
                codec='libx264',
                audio_codec='aac',
                bitrate=settings['bitrate'],
                verbose=False,
                logger=None
            )
        
        end_time = time.time()
        conversion_time = end_time - start_time
        
        # Calcular tamaños
        original_size = os.path.getsize(input_path) / (1024*1024)  # MB
        new_size = os.path.getsize(output_path) / (1024*1024)  # MB
        
        conversion_status[file_id].update({
            'status': 'completed',
            'progress': 100,
            'message': f'¡Conversión completada en {conversion_time:.1f} segundos!',
            'original_size': f'{original_size:.1f} MB',
            'new_size': f'{new_size:.1f} MB',
            'conversion_time': f'{conversion_time:.1f}s'
        })
        
    except Exception as e:
        conversion_status[file_id].update({
            'status': 'error',
            'progress': 0,
            'message': f'Error: {str(e)}'
        })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    
    file = request.files['file']
    quality = request.form.get('quality', 'medium')
    
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    
    if file and allowed_file(file.filename):
        # Generar ID único para el archivo
        file_id = str(uuid.uuid4())
        
        # Nombres de archivo seguros
        original_filename = secure_filename(file.filename)
        input_filename = f"{file_id}_{original_filename}"
        output_filename = f"{file_id}_{Path(original_filename).stem}.mp4"
        
        input_path = os.path.join(UPLOAD_FOLDER, input_filename)
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        # Guardar archivo
        file.save(input_path)
        
        # Inicializar estado de conversión
        conversion_status[file_id] = {
            'status': 'uploaded',
            'progress': 0,
            'message': 'Archivo subido correctamente',
            'original_filename': original_filename,
            'output_filename': output_filename,
            'quality': quality
        }
        
        # Iniciar conversión en hilo separado
        thread = threading.Thread(
            target=convert_video,
            args=(file_id, input_path, output_path, quality)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'success': True,
            'file_id': file_id,
            'message': 'Archivo subido, iniciando conversión...'
        })
    
    return jsonify({'error': 'Solo se permiten archivos WEBM'}), 400

@app.route('/status/<file_id>')
def check_status(file_id):
    if file_id in conversion_status:
        return jsonify(conversion_status[file_id])
    return jsonify({'error': 'Archivo no encontrado'}), 404

@app.route('/download/<file_id>')
def download_file(file_id):
    if file_id in conversion_status and conversion_status[file_id]['status'] == 'completed':
        output_filename = conversion_status[file_id]['output_filename']
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        if os.path.exists(output_path):
            return send_file(
                output_path,
                as_attachment=True,
                download_name=output_filename
            )
    
    return jsonify({'error': 'Archivo no disponible'}), 404

@app.route('/cleanup/<file_id>')
def cleanup_files(file_id):
    """Limpiar archivos después de la descarga"""
    if file_id in conversion_status:
        # Eliminar archivos
        try:
            input_filename = f"{file_id}_{conversion_status[file_id]['original_filename']}"
            output_filename = conversion_status[file_id]['output_filename']
            
            input_path = os.path.join(UPLOAD_FOLDER, input_filename)
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)
            
            if os.path.exists(input_path):
                os.remove(input_path)
            if os.path.exists(output_path):
                os.remove(output_path)
            
            # Limpiar estado
            del conversion_status[file_id]
            
        except Exception as e:
            pass
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
