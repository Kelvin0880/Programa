#!/usr/bin/env python3
"""
Conversor de Videos WEBM a MP4
================================

Este programa convierte archivos de video WEBM a formato MP4 usando moviepy.
Soporta conversión de archivos individuales o procesamiento en lote de carpetas.

Autor: Asistente IA
Fecha: Julio 2025
"""

import os
import sys
import argparse
from pathlib import Path
from moviepy.editor import VideoFileClip
import time

class WebmToMp4Converter:
    def __init__(self):
        self.converted_count = 0
        self.failed_count = 0
        self.failed_files = []

    def convert_single_file(self, input_path, output_path=None, quality='medium'):
        """
        Convierte un solo archivo WEBM a MP4
        
        Args:
            input_path (str): Ruta del archivo WEBM de entrada
            output_path (str): Ruta del archivo MP4 de salida (opcional)
            quality (str): Calidad de la conversión ('low', 'medium', 'high')
        
        Returns:
            bool: True si la conversión fue exitosa, False en caso contrario
        """
        try:
            input_path = Path(input_path)
            
            # Verificar que el archivo existe y es WEBM
            if not input_path.exists():
                print(f"❌ Error: El archivo {input_path} no existe.")
                return False
            
            if input_path.suffix.lower() != '.webm':
                print(f"⚠️  Advertencia: {input_path} no es un archivo WEBM.")
                return False
            
            # Generar nombre de salida si no se proporciona
            if output_path is None:
                output_path = input_path.with_suffix('.mp4')
            else:
                output_path = Path(output_path)
            
            print(f"🎬 Convirtiendo: {input_path.name} -> {output_path.name}")
            
            # Configurar calidad de video
            quality_settings = {
                'low': {'bitrate': '500k'},
                'medium': {'bitrate': '1000k'},
                'high': {'bitrate': '2000k'}
            }
            
            settings = quality_settings.get(quality, quality_settings['medium'])
            
            # Cargar el video y convertir
            with VideoFileClip(str(input_path)) as video:
                # Obtener información del video
                duration = video.duration
                fps = video.fps
                resolution = f"{video.w}x{video.h}"
                
                print(f"   📊 Duración: {duration:.2f}s, FPS: {fps}, Resolución: {resolution}")
                
                start_time = time.time()
                
                # Escribir el archivo MP4
                video.write_videofile(
                    str(output_path),
                    codec='libx264',
                    audio_codec='aac',
                    bitrate=settings['bitrate'],
                    verbose=False,
                    logger=None
                )
                
                end_time = time.time()
                conversion_time = end_time - start_time
                
                print(f"✅ Conversión completada en {conversion_time:.2f} segundos")
                print(f"   📁 Archivo guardado en: {output_path}")
                
                self.converted_count += 1
                return True
                
        except Exception as e:
            print(f"❌ Error al convertir {input_path}: {str(e)}")
            self.failed_count += 1
            self.failed_files.append(str(input_path))
            return False

    def convert_folder(self, folder_path, output_folder=None, quality='medium', recursive=False):
        """
        Convierte todos los archivos WEBM en una carpeta
        
        Args:
            folder_path (str): Ruta de la carpeta con archivos WEBM
            output_folder (str): Carpeta de salida (opcional)
            quality (str): Calidad de la conversión
            recursive (bool): Buscar archivos recursivamente en subcarpetas
        """
        folder_path = Path(folder_path)
        
        if not folder_path.exists() or not folder_path.is_dir():
            print(f"❌ Error: La carpeta {folder_path} no existe.")
            return
        
        # Configurar carpeta de salida
        if output_folder is None:
            output_folder = folder_path / "converted_mp4"
        else:
            output_folder = Path(output_folder)
        
        output_folder.mkdir(exist_ok=True)
        
        # Buscar archivos WEBM
        pattern = "**/*.webm" if recursive else "*.webm"
        webm_files = list(folder_path.glob(pattern))
        
        if not webm_files:
            print(f"⚠️  No se encontraron archivos WEBM en {folder_path}")
            return
        
        print(f"🔍 Encontrados {len(webm_files)} archivos WEBM")
        print(f"📁 Carpeta de salida: {output_folder}")
        print("=" * 50)
        
        for i, webm_file in enumerate(webm_files, 1):
            print(f"\n[{i}/{len(webm_files)}] Procesando archivo...")
            
            # Mantener estructura de carpetas si es recursivo
            if recursive:
                relative_path = webm_file.relative_to(folder_path)
                output_path = output_folder / relative_path.with_suffix('.mp4')
                output_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_path = output_folder / webm_file.with_suffix('.mp4').name
            
            self.convert_single_file(webm_file, output_path, quality)

    def print_summary(self):
        """Imprime un resumen de la conversión"""
        print("\n" + "=" * 50)
        print("📊 RESUMEN DE CONVERSIÓN")
        print("=" * 50)
        print(f"✅ Archivos convertidos exitosamente: {self.converted_count}")
        print(f"❌ Archivos que fallaron: {self.failed_count}")
        
        if self.failed_files:
            print("\n🚫 Archivos que fallaron:")
            for file in self.failed_files:
                print(f"   - {file}")

def main():
    parser = argparse.ArgumentParser(
        description="Conversor de videos WEBM a MP4",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python webm_to_mp4_converter.py archivo.webm
  python webm_to_mp4_converter.py archivo.webm -o salida.mp4
  python webm_to_mp4_converter.py -f /ruta/carpeta -q high
  python webm_to_mp4_converter.py -f /ruta/carpeta -r -o /ruta/salida
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('input_file', nargs='?', help='Archivo WEBM a convertir')
    group.add_argument('-f', '--folder', help='Carpeta con archivos WEBM')
    
    parser.add_argument('-o', '--output', help='Archivo o carpeta de salida')
    parser.add_argument('-q', '--quality', choices=['low', 'medium', 'high'], 
                       default='medium', help='Calidad de conversión (default: medium)')
    parser.add_argument('-r', '--recursive', action='store_true', 
                       help='Buscar archivos recursivamente en subcarpetas')
    
    args = parser.parse_args()
    
    # Crear el conversor
    converter = WebmToMp4Converter()
    
    print("🎬 Conversor WEBM a MP4")
    print("=" * 30)
    
    try:
        if args.input_file:
            # Conversión de archivo único
            success = converter.convert_single_file(args.input_file, args.output, args.quality)
            if not success:
                sys.exit(1)
        else:
            # Conversión de carpeta
            converter.convert_folder(args.folder, args.output, args.quality, args.recursive)
        
        converter.print_summary()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Conversión interrumpida por el usuario.")
        converter.print_summary()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
