@echo off
title Instalador - Conversor WEBM a MP4
color 0A

echo ========================================
echo  🎬 Conversor WEBM a MP4 - Instalador
echo ========================================
echo.
echo   Instalando componentes necesarios...
echo.

echo 🔍 Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python no está instalado o no está en el PATH.
    echo.
    echo 📥 Por favor, instala Python desde https://python.org
    echo ⚠️  IMPORTANTE: Marca "Add to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% encontrado

echo.
echo 📦 Actualizando pip...
python -m pip install --upgrade pip --quiet

echo.
echo 🔧 Instalando dependencias...
echo    - MoviePy (conversión de video)
echo    - TkinterDnD2 (arrastrar y soltar)
echo    - Pillow (procesamiento de imágenes)
echo    - ImageIO (codecs de video)

pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ❌ Error al instalar las dependencias.
    echo 💡 Intenta ejecutar como administrador
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ ¡Instalación completada exitosamente!
echo.
echo 🎯 Modos de uso disponibles:
echo.
echo   1️⃣  INTERFAZ GRÁFICA (Recomendado):
echo      👉 Ejecuta: iniciar_interfaz.bat
echo      💡 Arrastra archivos, selecciona carpetas, muy fácil
echo.
echo   2️⃣  LÍNEA DE COMANDOS:
echo      👉 Ejecuta: python webm_to_mp4_converter.py archivo.webm
echo      💡 Para usuarios avanzados
echo.
echo   3️⃣  MENÚ INTERACTIVO:
echo      👉 Ejecuta: ejemplos.bat
echo      💡 Menú paso a paso
echo.
echo ================================================
echo 🚀 ¡Listo para convertir tus videos WEBM a MP4!
echo ================================================
echo.
pause
