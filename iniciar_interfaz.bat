@echo off
title Conversor WEBM a MP4 - Interfaz Gráfica
color 0B

echo.
echo ================================================
echo          🎬 CONVERSOR WEBM A MP4 🎬
echo ================================================
echo.
echo        Interfaz Gráfica Moderna
echo        Arrastra y suelta tus archivos
echo.
echo ================================================
echo.

echo 🔍 Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python no está instalado o no está en el PATH.
    echo.
    echo 📥 Descarga Python desde: https://python.org
    echo ⚠️  Asegúrate de marcar "Add to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado

echo.
echo 📦 Verificando dependencias...
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Tkinter no está disponible
    echo 💡 Instala la versión completa de Python desde python.org
    pause
    exit /b 1
)

echo ✅ Tkinter disponible

python -c "import moviepy" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  MoviePy no encontrado, instalando dependencias...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ Error al instalar dependencias
        pause
        exit /b 1
    )
    echo ✅ Dependencias instaladas
) else (
    echo ✅ Dependencias disponibles
)

echo.
echo 🚀 Iniciando interfaz gráfica...
echo.

REM Intentar primero la versión completa con drag and drop
python webm_converter_gui.py >nul 2>&1

REM Si falla, usar la versión simplificada
if %errorlevel% neq 0 (
    echo ⚠️  Usando versión simplificada (sin drag and drop)
    python webm_converter_simple.py
) else (
    echo ✅ Interfaz completa iniciada
)

if %errorlevel% neq 0 (
    echo.
    echo ❌ Error al ejecutar la aplicación
    echo 💡 Verifica que todos los archivos estén presentes
    pause
)

echo.
echo 👋 ¡Hasta luego!
timeout /t 3 >nul
