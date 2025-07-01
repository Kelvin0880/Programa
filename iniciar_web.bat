@echo off
title Conversor WEBM a MP4 - Aplicación Web
color 0B

echo.
echo ================================================
echo     🌐 CONVERSOR WEBM A MP4 - WEB APP 🌐
echo ================================================
echo.
echo   ✨ Aplicación web para usar desde cualquier
echo      dispositivo: móvil, tablet, computadora
echo.
echo ================================================
echo.

echo 🔍 Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python no está instalado
    pause
    exit /b 1
)

echo ✅ Python encontrado

echo.
echo 📦 Verificando dependencias web...
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo 📥 Instalando Flask...
    pip install Flask==2.3.3 Werkzeug==2.3.7
    if %errorlevel% neq 0 (
        echo ❌ Error al instalar Flask
        pause
        exit /b 1
    )
)

echo ✅ Flask disponible

echo.
echo 🚀 Iniciando servidor web...
echo.
echo ================================================
echo            📱 INSTRUCCIONES DE USO 📱
echo ================================================
echo.
echo 🌐 ABRIR EN NAVEGADOR:
echo    👉 http://localhost:5000
echo.
echo 📱 USAR EN MÓVIL (misma red WiFi):
echo    1. Busca la IP de tu PC (ipconfig)
echo    2. Usa: http://[IP-DE-TU-PC]:5000
echo    3. Ejemplo: http://192.168.1.100:5000
echo.
echo 🎯 FUNCIONES DISPONIBLES:
echo    • Arrastrar y soltar archivos WEBM
echo    • Seleccionar archivos desde dispositivo
echo    • Elegir calidad de conversión
echo    • Progreso en tiempo real
echo    • Descarga automática del MP4
echo.
echo ⚠️  IMPORTANTE:
echo    • Mantén esta ventana abierta
echo    • Presiona Ctrl+C para detener
echo    • No cierres hasta terminar conversiones
echo.
echo ================================================
echo 🚀 SERVIDOR INICIANDO...
echo ================================================
echo.

python web_app.py
