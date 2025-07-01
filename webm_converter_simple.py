#!/usr/bin/env python3
"""
Conversor WEBM a MP4 - Interfaz Gráfica Simplificada
====================================================

Versión simplificada que no requiere tkinterdnd2 para drag and drop,
pero mantiene una interfaz moderna y funcional.

Autor: Asistente IA
Fecha: Julio 2025
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from pathlib import Path
from moviepy.editor import VideoFileClip
import time

class SimpleWebmConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎬 Conversor WEBM a MP4")
        self.root.geometry("800x700")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(True, True)
        self.root.state('zoomed')  # Maximizar al iniciar
        
        # Variables
        self.files_to_convert = []
        self.is_converting = False
        self.converted_count = 0
        self.failed_count = 0
        
        # Configurar el estilo
        self.setup_styles()
        
        # Crear la interfaz
        self.create_widgets()
        
        # Centrar la ventana
        self.center_window()

    def setup_styles(self):
        """Configurar estilos modernos para la interfaz"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos personalizados
        style.configure('Title.TLabel', 
                       background='#2c3e50', 
                       foreground='#ecf0f1',
                       font=('Arial', 18, 'bold'))
        
        style.configure('Modern.TButton',
                       font=('Arial', 11, 'bold'))
        
        style.configure('Big.TButton',
                       font=('Arial', 14, 'bold'))

    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal con padding
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True, padx=25, pady=25)
        
        # Título principal
        title_label = ttk.Label(main_frame, text="🎬 Conversor WEBM a MP4", style='Title.TLabel')
        title_label.pack(pady=(0, 30))
        
        # Sección de selección de archivos
        self.create_file_selection(main_frame)
        
        # Lista de archivos
        self.create_file_list(main_frame)
        
        # Configuración de calidad
        self.create_quality_settings(main_frame)
        
        # Área de progreso
        self.create_progress_area(main_frame)
        
        # Botón de conversión principal
        self.create_convert_button(main_frame)

    def create_file_selection(self, parent):
        """Crear sección de selección de archivos"""
        # Frame contenedor con borde
        selection_frame = tk.LabelFrame(
            parent, 
            text="  📁 Selección de Archivos  ",
            bg='#34495e', 
            fg='#ecf0f1',
            font=('Arial', 12, 'bold'),
            relief='raised',
            bd=2
        )
        selection_frame.pack(fill='x', pady=(0, 20))
        
        # Frame interno para los botones
        button_container = tk.Frame(selection_frame, bg='#34495e')
        button_container.pack(fill='x', padx=20, pady=15)
        
        # Botones de selección
        ttk.Button(
            button_container, 
            text="🎯 Seleccionar Archivos WEBM", 
            command=self.select_files,
            style='Modern.TButton'
        ).pack(side='left', padx=(0, 15))
        
        ttk.Button(
            button_container, 
            text="📂 Seleccionar Carpeta Completa", 
            command=self.select_folder,
            style='Modern.TButton'
        ).pack(side='left', padx=(0, 15))
        
        ttk.Button(
            button_container, 
            text="🗑️ Limpiar Todo", 
            command=self.clear_files,
            style='Modern.TButton'
        ).pack(side='right')

    def create_file_list(self, parent):
        """Crear la lista de archivos con mejor diseño"""
        list_frame = tk.LabelFrame(
            parent,
            text="  📋 Archivos para Convertir  ",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 12, 'bold'),
            relief='raised',
            bd=2
        )
        list_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # Container interno
        list_container = tk.Frame(list_frame, bg='#34495e')
        list_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_container)
        scrollbar.pack(side='right', fill='y')
        
        # Listbox mejorada
        self.file_listbox = tk.Listbox(
            list_container,
            bg='#2c3e50',
            fg='#ecf0f1',
            selectbackground='#3498db',
            selectforeground='white',
            font=('Arial', 10),
            yscrollcommand=scrollbar.set,
            relief='flat',
            bd=0
        )
        self.file_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Mensaje inicial
        self.file_listbox.insert(0, "👆 Usa los botones de arriba para agregar archivos WEBM")

    def create_quality_settings(self, parent):
        """Crear configuración de calidad con mejor diseño"""
        quality_frame = tk.LabelFrame(
            parent,
            text="  ⚙️ Configuración de Calidad  ",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 12, 'bold'),
            relief='raised',
            bd=2
        )
        quality_frame.pack(fill='x', pady=(0, 20))
        
        # Container interno
        quality_container = tk.Frame(quality_frame, bg='#34495e')
        quality_container.pack(fill='x', padx=20, pady=15)
        
        self.quality_var = tk.StringVar(value='medium')
        
        quality_options = [
            ('🔹 Calidad Baja (Archivos pequeños, 500k bitrate)', 'low'),
            ('🔸 Calidad Media (Balance perfecto, 1000k bitrate)', 'medium'),
            ('🔶 Calidad Alta (Mejor calidad, 2000k bitrate)', 'high')
        ]
        
        for text, value in quality_options:
            rb = tk.Radiobutton(
                quality_container,
                text=text,
                variable=self.quality_var,
                value=value,
                bg='#34495e',
                fg='#ecf0f1',
                selectcolor='#2c3e50',
                activebackground='#34495e',
                activeforeground='#ecf0f1',
                font=('Arial', 10)
            )
            rb.pack(anchor='w', pady=3)

    def create_progress_area(self, parent):
        """Crear área de progreso mejorada"""
        progress_frame = tk.LabelFrame(
            parent,
            text="  📊 Progreso de Conversión  ",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 12, 'bold'),
            relief='raised',
            bd=2
        )
        progress_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # Container interno
        progress_container = tk.Frame(progress_frame, bg='#34495e')
        progress_container.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Etiqueta de estado
        self.progress_label = tk.Label(
            progress_container,
            text="✨ Listo para convertir tus videos",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 11, 'bold')
        )
        self.progress_label.pack(anchor='w', pady=(0, 10))
        
        # Barra de progreso
        self.progress_bar = ttk.Progressbar(
            progress_container,
            mode='determinate',
            length=400
        )
        self.progress_bar.pack(fill='x', pady=(0, 15))
        
        # Área de logs
        log_container = tk.Frame(progress_container, bg='#2c3e50', relief='sunken', bd=1)
        log_container.pack(fill='both', expand=True)
        
        log_scrollbar = ttk.Scrollbar(log_container)
        log_scrollbar.pack(side='right', fill='y')
        
        self.log_text = tk.Text(
            log_container,
            bg='#2c3e50',
            fg='#ecf0f1',
            font=('Consolas', 9),
            height=6,
            yscrollcommand=log_scrollbar.set,
            wrap=tk.WORD,
            relief='flat',
            bd=0
        )
        self.log_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        log_scrollbar.config(command=self.log_text.yview)
        
        # Mensaje inicial en el log
        self.log_message("🎬 Conversor WEBM a MP4 iniciado")
        self.log_message("💡 Selecciona archivos y presiona 'Convertir' para comenzar")

    def create_convert_button(self, parent):
        """Crear botón de conversión principal"""
        button_frame = tk.Frame(parent, bg='#2c3e50')
        button_frame.pack(fill='x')
        
        self.convert_button = ttk.Button(
            button_frame,
            text="🚀 ¡CONVERTIR ARCHIVOS AHORA!",
            command=self.start_conversion,
            style='Big.TButton'
        )
        self.convert_button.pack(pady=10)

    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def select_files(self):
        """Seleccionar archivos WEBM"""
        files = filedialog.askopenfilenames(
            title="🎯 Seleccionar archivos WEBM para convertir",
            filetypes=[
                ("Archivos WEBM", "*.webm"),
                ("Todos los archivos", "*.*")
            ]
        )
        if files:
            self.add_files(files)

    def select_folder(self):
        """Seleccionar carpeta con archivos WEBM"""
        folder = filedialog.askdirectory(
            title="📂 Seleccionar carpeta con archivos WEBM"
        )
        if folder:
            webm_files = list(Path(folder).glob("*.webm"))
            if webm_files:
                self.add_files([str(f) for f in webm_files])
                self.log_message(f"✅ Encontrados {len(webm_files)} archivos WEBM en: {Path(folder).name}")
            else:
                messagebox.showinfo(
                    "Sin archivos WEBM", 
                    f"No se encontraron archivos WEBM en la carpeta:\n{folder}"
                )

    def add_files(self, files):
        """Agregar archivos a la lista"""
        # Limpiar mensaje inicial si existe
        if self.file_listbox.size() == 1 and "👆 Usa los botones" in self.file_listbox.get(0):
            self.file_listbox.delete(0)
        
        added_count = 0
        for file_path in files:
            if file_path.lower().endswith('.webm') and file_path not in self.files_to_convert:
                self.files_to_convert.append(file_path)
                # Mostrar solo el nombre del archivo para mejor legibilidad
                file_name = Path(file_path).name
                self.file_listbox.insert(tk.END, f"📁 {file_name}")
                added_count += 1
        
        if added_count > 0:
            self.log_message(f"✅ Agregados {added_count} archivos nuevos")
            self.log_message(f"📊 Total de archivos en lista: {len(self.files_to_convert)}")

    def clear_files(self):
        """Limpiar la lista de archivos"""
        if self.files_to_convert:
            result = messagebox.askyesno(
                "Confirmar limpieza",
                f"¿Estás seguro de querer limpiar la lista?\n\nSe eliminarán {len(self.files_to_convert)} archivos de la lista."
            )
            if result:
                self.files_to_convert.clear()
                self.file_listbox.delete(0, tk.END)
                self.file_listbox.insert(0, "👆 Usa los botones de arriba para agregar archivos WEBM")
                self.log_message("🗑️ Lista de archivos limpiada")

    def log_message(self, message):
        """Agregar mensaje al log con timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def start_conversion(self):
        """Iniciar proceso de conversión"""
        if not self.files_to_convert:
            messagebox.showwarning(
                "Sin archivos para convertir",
                "❌ No hay archivos WEBM en la lista.\n\n💡 Usa los botones para agregar archivos primero."
            )
            return
        
        if self.is_converting:
            messagebox.showinfo(
                "Conversión en progreso",
                "⏳ Ya hay una conversión en progreso.\n\n⏳ Por favor espera a que termine."
            )
            return
        
        # Confirmar inicio de conversión
        result = messagebox.askyesno(
            "Confirmar conversión",
            f"🎬 ¿Iniciar conversión de {len(self.files_to_convert)} archivos?\n\n"
            f"⚙️ Calidad seleccionada: {self.quality_var.get().upper()}\n"
            f"📁 Los archivos MP4 se guardarán en la misma carpeta que los originales."
        )
        
        if result:
            self.is_converting = True
            self.convert_button.config(
                text="⏳ CONVIRTIENDO... (No cerrar ventana)",
                state='disabled'
            )
            
            # Iniciar conversión en hilo separado
            thread = threading.Thread(target=self.convert_files)
            thread.daemon = True
            thread.start()

    def convert_files(self):
        """Convertir todos los archivos (ejecutado en hilo separado)"""
        self.converted_count = 0
        self.failed_count = 0
        total_files = len(self.files_to_convert)
        
        self.log_message("=" * 40)
        self.log_message(f"🚀 INICIANDO CONVERSIÓN DE {total_files} ARCHIVOS")
        self.log_message(f"⚙️ Calidad: {self.quality_var.get().upper()}")
        self.log_message("=" * 40)
        
        for i, file_path in enumerate(self.files_to_convert):
            try:
                # Actualizar progreso
                progress = ((i + 1) / total_files) * 100
                self.progress_bar['value'] = progress
                
                file_name = Path(file_path).name
                self.progress_label.config(
                    text=f"🎬 Convirtiendo [{i+1}/{total_files}]: {file_name}"
                )
                
                # Convertir archivo
                self.convert_single_file(file_path)
                
            except Exception as e:
                error_msg = f"❌ Error en {Path(file_path).name}: {str(e)}"
                self.log_message(error_msg)
                self.failed_count += 1
        
        # Finalizar conversión
        self.progress_bar['value'] = 100
        self.progress_label.config(text="✅ ¡Conversión completada!")
        
        self.is_converting = False
        self.convert_button.config(
            text="🚀 ¡CONVERTIR ARCHIVOS AHORA!",
            state='normal'
        )
        
        # Mostrar resumen
        self.show_final_summary()

    def convert_single_file(self, input_path):
        """Convertir un archivo individual"""
        input_path = Path(input_path)
        output_path = input_path.with_suffix('.mp4')
        
        # Configuración de calidad
        quality_settings = {
            'low': {'bitrate': '500k', 'desc': 'Baja'},
            'medium': {'bitrate': '1000k', 'desc': 'Media'},
            'high': {'bitrate': '2000k', 'desc': 'Alta'}
        }
        
        settings = quality_settings[self.quality_var.get()]
        
        self.log_message(f"🎬 Procesando: {input_path.name}")
        
        start_time = time.time()
        
        try:
            with VideoFileClip(str(input_path)) as video:
                # Información del video
                duration = video.duration
                self.log_message(f"   📊 Duración: {duration:.1f}s | Calidad: {settings['desc']}")
                
                # Realizar conversión
                video.write_videofile(
                    str(output_path),
                    codec='libx264',
                    audio_codec='aac',
                    bitrate=settings['bitrate'],
                    verbose=False,
                    logger=None
                )
            
            # Calcular tiempo y tamaños
            end_time = time.time()
            conversion_time = end_time - start_time
            
            original_size = input_path.stat().st_size / (1024*1024)  # MB
            new_size = output_path.stat().st_size / (1024*1024)  # MB
            
            self.log_message(f"   ✅ Completado en {conversion_time:.1f}s")
            self.log_message(f"   📁 {original_size:.1f}MB → {new_size:.1f}MB")
            
            self.converted_count += 1
            
        except Exception as e:
            self.log_message(f"   ❌ Error: {str(e)}")
            self.failed_count += 1
            raise

    def show_final_summary(self):
        """Mostrar resumen final de la conversión"""
        total = self.converted_count + self.failed_count
        
        self.log_message("=" * 40)
        self.log_message("📊 RESUMEN FINAL DE CONVERSIÓN")
        self.log_message(f"✅ Archivos convertidos exitosamente: {self.converted_count}")
        self.log_message(f"❌ Archivos con errores: {self.failed_count}")
        self.log_message(f"📊 Total procesado: {total}")
        self.log_message("=" * 40)
        
        # Ventana de resumen
        if self.failed_count == 0:
            messagebox.showinfo(
                "🎉 ¡Conversión Exitosa!",
                f"🎊 ¡Felicidades! Todos los archivos fueron convertidos exitosamente.\n\n"
                f"✅ Archivos convertidos: {self.converted_count}\n"
                f"📁 Los archivos MP4 están en las mismas carpetas que los originales.\n\n"
                f"🎬 ¡Disfruta tus videos!"
            )
        else:
            messagebox.showwarning(
                "⚠️ Conversión Completada con Algunos Errores",
                f"📊 Resumen de conversión:\n\n"
                f"✅ Exitosos: {self.converted_count}\n"
                f"❌ Con errores: {self.failed_count}\n\n"
                f"💡 Revisa el log para ver los detalles de los errores."
            )

    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

def main():
    """Función principal"""
    try:
        app = SimpleWebmConverter()
        app.run()
    except Exception as e:
        messagebox.showerror(
            "Error crítico",
            f"❌ Error al iniciar la aplicación:\n\n{str(e)}\n\n"
            f"💡 Verifica que todas las dependencias estén instaladas."
        )

if __name__ == "__main__":
    main()
