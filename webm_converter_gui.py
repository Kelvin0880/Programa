#!/usr/bin/env python3
"""
Conversor WEBM a MP4 - Interfaz Gráfica
=======================================

Aplicación con interfaz gráfica moderna para convertir archivos WEBM a MP4.
Soporta arrastrar y soltar archivos, selección de archivos y carpetas.

Autor: Asistente IA
Fecha: Julio 2025
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import threading
from pathlib import Path
from moviepy.editor import VideoFileClip
import time

class ModernWebmConverter:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("🎬 Conversor WEBM a MP4")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(True, True)
        
        # Variables
        self.files_to_convert = []
        self.is_converting = False
        self.converted_count = 0
        self.failed_count = 0
        
        # Configurar el estilo
        self.setup_styles()
        
        # Crear la interfaz
        self.create_widgets()
        
        # Configurar drag and drop
        self.setup_drag_drop()
        
        # Centrar la ventana
        self.center_window()

    def setup_styles(self):
        """Configurar estilos modernos para la interfaz"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores modernos
        colors = {
            'bg': '#2c3e50',
            'fg': '#ecf0f1',
            'accent': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'dark': '#34495e'
        }
        
        # Configurar estilos
        style.configure('Title.TLabel', 
                       background=colors['bg'], 
                       foreground=colors['fg'],
                       font=('Arial', 16, 'bold'))
        
        style.configure('Modern.TButton',
                       background=colors['accent'],
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       font=('Arial', 10, 'bold'))
        
        style.map('Modern.TButton',
                 background=[('active', '#2980b9')])
        
        style.configure('Success.TButton',
                       background=colors['success'],
                       foreground='white',
                       borderwidth=0,
                       font=('Arial', 10, 'bold'))
        
        style.configure('Danger.TButton',
                       background=colors['danger'],
                       foreground='white',
                       borderwidth=0,
                       font=('Arial', 10, 'bold'))

    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Título
        title_label = ttk.Label(main_frame, text="🎬 Conversor WEBM a MP4", style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Área de drag and drop
        self.create_drop_area(main_frame)
        
        # Botones de acción
        self.create_action_buttons(main_frame)
        
        # Lista de archivos
        self.create_file_list(main_frame)
        
        # Configuración de calidad
        self.create_quality_settings(main_frame)
        
        # Área de progreso
        self.create_progress_area(main_frame)
        
        # Botón de conversión
        self.create_convert_button(main_frame)

    def create_drop_area(self, parent):
        """Crear el área de arrastrar y soltar"""
        drop_frame = tk.Frame(parent, bg='#34495e', relief='raised', bd=2)
        drop_frame.pack(fill='x', pady=(0, 20))
        
        self.drop_label = tk.Label(
            drop_frame,
            text="🎯 Arrastra aquí tus archivos WEBM\no haz clic para seleccionar",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 14, 'bold'),
            pady=40
        )
        self.drop_label.pack(fill='both', expand=True)
        
        # Hacer el área clickeable
        self.drop_label.bind('<Button-1>', self.select_files)
        drop_frame.bind('<Button-1>', self.select_files)

    def create_action_buttons(self, parent):
        """Crear botones de acción"""
        button_frame = tk.Frame(parent, bg='#2c3e50')
        button_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Button(button_frame, text="📁 Seleccionar Archivos", 
                  command=self.select_files, style='Modern.TButton').pack(side='left', padx=(0, 10))
        
        ttk.Button(button_frame, text="📂 Seleccionar Carpeta", 
                  command=self.select_folder, style='Modern.TButton').pack(side='left', padx=(0, 10))
        
        ttk.Button(button_frame, text="🗑️ Limpiar Lista", 
                  command=self.clear_files, style='Danger.TButton').pack(side='right')

    def create_file_list(self, parent):
        """Crear la lista de archivos"""
        list_frame = tk.Frame(parent, bg='#2c3e50')
        list_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        # Etiqueta
        tk.Label(list_frame, text="📋 Archivos a convertir:", 
                bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Frame con scrollbar
        list_container = tk.Frame(list_frame, bg='#34495e')
        list_container.pack(fill='both', expand=True, pady=(10, 0))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_container)
        scrollbar.pack(side='right', fill='y')
        
        # Listbox
        self.file_listbox = tk.Listbox(
            list_container,
            bg='#34495e',
            fg='#ecf0f1',
            selectbackground='#3498db',
            selectforeground='white',
            font=('Arial', 10),
            yscrollcommand=scrollbar.set
        )
        self.file_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.file_listbox.yview)

    def create_quality_settings(self, parent):
        """Crear configuración de calidad"""
        quality_frame = tk.Frame(parent, bg='#2c3e50')
        quality_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(quality_frame, text="⚙️ Calidad de conversión:", 
                bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12, 'bold')).pack(side='left')
        
        self.quality_var = tk.StringVar(value='medium')
        quality_options = [
            ('🔹 Baja (500k)', 'low'),
            ('🔸 Media (1000k)', 'medium'),
            ('🔶 Alta (2000k)', 'high')
        ]
        
        for text, value in quality_options:
            tk.Radiobutton(
                quality_frame,
                text=text,
                variable=self.quality_var,
                value=value,
                bg='#2c3e50',
                fg='#ecf0f1',
                selectcolor='#34495e',
                activebackground='#2c3e50',
                activeforeground='#ecf0f1',
                font=('Arial', 10)
            ).pack(side='left', padx=(20, 0))

    def create_progress_area(self, parent):
        """Crear área de progreso"""
        progress_frame = tk.Frame(parent, bg='#2c3e50')
        progress_frame.pack(fill='x', pady=(0, 20))
        
        # Etiqueta de progreso
        self.progress_label = tk.Label(
            progress_frame,
            text="📊 Listo para convertir",
            bg='#2c3e50',
            fg='#ecf0f1',
            font=('Arial', 11)
        )
        self.progress_label.pack(anchor='w')
        
        # Barra de progreso
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            length=400
        )
        self.progress_bar.pack(fill='x', pady=(10, 0))
        
        # Área de logs
        log_container = tk.Frame(progress_frame, bg='#34495e')
        log_container.pack(fill='both', expand=True, pady=(10, 0))
        
        log_scrollbar = ttk.Scrollbar(log_container)
        log_scrollbar.pack(side='right', fill='y')
        
        self.log_text = tk.Text(
            log_container,
            bg='#34495e',
            fg='#ecf0f1',
            font=('Consolas', 9),
            height=8,
            yscrollcommand=log_scrollbar.set
        )
        self.log_text.pack(side='left', fill='both', expand=True)
        log_scrollbar.config(command=self.log_text.yview)

    def create_convert_button(self, parent):
        """Crear botón de conversión"""
        self.convert_button = ttk.Button(
            parent,
            text="🚀 Convertir Archivos",
            command=self.start_conversion,
            style='Success.TButton'
        )
        self.convert_button.pack(pady=(10, 0))

    def setup_drag_drop(self):
        """Configurar drag and drop"""
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.handle_drop)

    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def handle_drop(self, event):
        """Manejar archivos arrastrados"""
        files = self.root.tk.splitlist(event.data)
        self.add_files(files)

    def select_files(self, event=None):
        """Seleccionar archivos manualmente"""
        files = filedialog.askopenfilenames(
            title="Seleccionar archivos WEBM",
            filetypes=[("Archivos WEBM", "*.webm"), ("Todos los archivos", "*.*")]
        )
        if files:
            self.add_files(files)

    def select_folder(self):
        """Seleccionar una carpeta"""
        folder = filedialog.askdirectory(title="Seleccionar carpeta con archivos WEBM")
        if folder:
            webm_files = list(Path(folder).glob("*.webm"))
            if webm_files:
                self.add_files([str(f) for f in webm_files])
                self.log_message(f"✅ Encontrados {len(webm_files)} archivos WEBM en la carpeta")
            else:
                messagebox.showwarning("Sin archivos", "No se encontraron archivos WEBM en la carpeta seleccionada")

    def add_files(self, files):
        """Agregar archivos a la lista"""
        added_count = 0
        for file_path in files:
            if file_path.lower().endswith('.webm') and file_path not in self.files_to_convert:
                self.files_to_convert.append(file_path)
                self.file_listbox.insert(tk.END, Path(file_path).name)
                added_count += 1
        
        if added_count > 0:
            self.log_message(f"✅ Agregados {added_count} archivos a la lista")
            self.update_drop_label()

    def clear_files(self):
        """Limpiar la lista de archivos"""
        self.files_to_convert.clear()
        self.file_listbox.delete(0, tk.END)
        self.update_drop_label()
        self.log_message("🗑️ Lista de archivos limpiada")

    def update_drop_label(self):
        """Actualizar el texto del área de drop"""
        count = len(self.files_to_convert)
        if count == 0:
            self.drop_label.config(text="🎯 Arrastra aquí tus archivos WEBM\no haz clic para seleccionar")
        else:
            self.drop_label.config(text=f"📁 {count} archivo{'s' if count != 1 else ''} listo{'s' if count != 1 else ''} para convertir")

    def log_message(self, message):
        """Agregar mensaje al log"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def start_conversion(self):
        """Iniciar la conversión en un hilo separado"""
        if not self.files_to_convert:
            messagebox.showwarning("Sin archivos", "No hay archivos para convertir")
            return
        
        if self.is_converting:
            messagebox.showinfo("Conversión en progreso", "Ya hay una conversión en progreso")
            return
        
        # Iniciar conversión en hilo separado
        self.is_converting = True
        self.convert_button.config(text="⏳ Convirtiendo...", state='disabled')
        
        thread = threading.Thread(target=self.convert_files)
        thread.daemon = True
        thread.start()

    def convert_files(self):
        """Convertir todos los archivos"""
        self.converted_count = 0
        self.failed_count = 0
        total_files = len(self.files_to_convert)
        
        self.log_message(f"🚀 Iniciando conversión de {total_files} archivos...")
        
        for i, file_path in enumerate(self.files_to_convert):
            try:
                # Actualizar progreso
                progress = (i / total_files) * 100
                self.progress_bar['value'] = progress
                self.progress_label.config(text=f"📊 Convirtiendo {i+1}/{total_files}: {Path(file_path).name}")
                
                # Convertir archivo
                self.convert_single_file(file_path)
                
            except Exception as e:
                self.log_message(f"❌ Error al convertir {Path(file_path).name}: {str(e)}")
                self.failed_count += 1
        
        # Finalizar
        self.progress_bar['value'] = 100
        self.is_converting = False
        self.convert_button.config(text="🚀 Convertir Archivos", state='normal')
        
        # Mostrar resumen
        self.show_summary()

    def convert_single_file(self, input_path):
        """Convertir un solo archivo"""
        input_path = Path(input_path)
        output_path = input_path.with_suffix('.mp4')
        
        # Configurar calidad
        quality_settings = {
            'low': {'bitrate': '500k'},
            'medium': {'bitrate': '1000k'},
            'high': {'bitrate': '2000k'}
        }
        
        settings = quality_settings[self.quality_var.get()]
        
        self.log_message(f"🎬 Convirtiendo: {input_path.name}")
        
        start_time = time.time()
        
        with VideoFileClip(str(input_path)) as video:
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
        
        self.log_message(f"✅ Completado en {conversion_time:.2f}s: {output_path.name}")
        self.converted_count += 1

    def show_summary(self):
        """Mostrar resumen de la conversión"""
        total = self.converted_count + self.failed_count
        
        self.log_message("=" * 50)
        self.log_message(f"📊 RESUMEN DE CONVERSIÓN")
        self.log_message(f"✅ Exitosos: {self.converted_count}/{total}")
        self.log_message(f"❌ Fallidos: {self.failed_count}/{total}")
        self.log_message("=" * 50)
        
        # Mostrar ventana de resumen
        if self.failed_count == 0:
            messagebox.showinfo("¡Conversión Completada!", 
                              f"🎉 ¡Todos los archivos fueron convertidos exitosamente!\n\n"
                              f"Archivos convertidos: {self.converted_count}")
        else:
            messagebox.showwarning("Conversión Completada con Errores", 
                                 f"Conversión finalizada:\n\n"
                                 f"✅ Exitosos: {self.converted_count}\n"
                                 f"❌ Fallidos: {self.failed_count}\n\n"
                                 f"Revisa el log para más detalles.")

    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

def main():
    """Función principal"""
    try:
        app = ModernWebmConverter()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")

if __name__ == "__main__":
    main()
