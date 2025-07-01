@echo off
title Demo del Conversor WEBM a MP4
color 0E

echo.
echo ════════════════════════════════════════════════
echo          🎬 DEMO - CONVERSOR WEBM A MP4 🎬
echo ════════════════════════════════════════════════
echo.
echo   🎯 Demo interactivo del conversor de videos
echo.
echo ════════════════════════════════════════════════
echo.

:menu
echo.
echo 🎮 OPCIONES DE DEMO:
echo.
echo   1️⃣  Abrir Interfaz Gráfica (Recomendado)
echo   2️⃣  Mostrar características del programa
echo   3️⃣  Ver ejemplos de uso
echo   4️⃣  Información técnica
echo   5️⃣  Crear archivo de prueba WEBM (simulado)
echo   6️⃣  Ejecutar línea de comandos
echo   0️⃣  Salir
echo.
set /p choice="👆 Selecciona una opción (0-6): "

if "%choice%"=="1" goto gui_demo
if "%choice%"=="2" goto features
if "%choice%"=="3" goto examples
if "%choice%"=="4" goto technical
if "%choice%"=="5" goto create_test
if "%choice%"=="6" goto command_line
if "%choice%"=="0" goto exit
goto invalid

:gui_demo
echo.
echo 🚀 Abriendo Interfaz Gráfica...
echo.
echo 💡 En la interfaz podrás:
echo    • Seleccionar archivos WEBM individuales
echo    • Seleccionar carpetas completas
echo    • Configurar la calidad de conversión
echo    • Ver el progreso en tiempo real
echo    • Obtener estadísticas detalladas
echo.
pause
call iniciar_interfaz.bat
goto menu

:features
echo.
echo ✨ CARACTERÍSTICAS PRINCIPALES:
echo.
echo 🖼️  INTERFAZ GRÁFICA MODERNA:
echo    • Diseño elegante y profesional
echo    • Botones grandes y fáciles de usar
echo    • Tema oscuro agradable a la vista
echo    • Progreso visual en tiempo real
echo.
echo ⚙️  CONFIGURACIÓN AVANZADA:
echo    • 3 niveles de calidad (Baja/Media/Alta)
echo    • Conversión en segundo plano
echo    • Log detallado de operaciones
echo    • Manejo inteligente de errores
echo.
echo 📁 PROCESAMIENTO INTELIGENTE:
echo    • Archivos individuales o carpetas
echo    • Detección automática de archivos WEBM
echo    • Preservación de nombres originales
echo    • Estadísticas de conversión
echo.
pause
goto menu

:examples
echo.
echo 📝 EJEMPLOS DE USO TÍPICOS:
echo.
echo 🎬 PARA CREADORES DE CONTENIDO:
echo    • Convertir descargas de YouTube
echo    • Preparar videos para edición
echo    • Optimizar para diferentes plataformas
echo.
echo 📱 PARA USO PERSONAL:
echo    • Videos para WhatsApp/Telegram
echo    • Compatibilidad con todos los reproductores
echo    • Reducir tamaño de archivos
echo.
echo 💼 PARA USO PROFESIONAL:
echo    • Estandarizar formatos de video
echo    • Archivos para presentaciones
echo    • Compatibilidad con software profesional
echo.
echo 🎯 CASOS ESPECÍFICOS:
echo    • Video de 100MB → 60MB (calidad media)
echo    • Video 4K de 30 min → Conversión en 10 min
echo    • Lote de 50 videos → Procesamiento automático
echo.
pause
goto menu

:technical
echo.
echo 🔧 INFORMACIÓN TÉCNICA:
echo.
echo 📋 ESPECIFICACIONES:
echo    • Lenguaje: Python 3.6+
echo    • Interfaz: Tkinter (incluido en Python)
echo    • Motor de conversión: MoviePy + FFmpeg
echo    • Formatos: WEBM → MP4 (H.264/AAC)
echo    • Plataforma: Windows 7/8/10/11
echo.
echo ⚙️ CONFIGURACIONES DE CALIDAD:
echo    • Baja:  500k bitrate  → Archivos pequeños
echo    • Media: 1000k bitrate → Balance perfecto
echo    • Alta:  2000k bitrate → Máxima calidad
echo.
echo 🚀 RENDIMIENTO TÍPICO:
echo    • Video HD (10 min): 2-3 minutos de conversión
echo    • Video 4K (5 min):  5-8 minutos de conversión
echo    • Procesamiento: Multihilo para mejor rendimiento
echo.
echo 💾 REQUISITOS DEL SISTEMA:
echo    • RAM: Mínimo 2GB, recomendado 4GB+
echo    • Espacio: Mismo que el archivo original
echo    • CPU: Cualquier procesador moderno
echo.
pause
goto menu

:create_test
echo.
echo 🧪 CREAR ARCHIVO DE PRUEBA:
echo.
echo 💡 Para probar el conversor, puedes:
echo.
echo 1️⃣  Descargar un video WEBM desde:
echo    • YouTube (usando youtube-dl o similares)
echo    • Sitios web que generen archivos WEBM
echo    • Grabar pantalla en formato WEBM
echo.
echo 2️⃣  O usar archivos WEBM existentes de:
echo    • Carpeta de Descargas
echo    • Grabaciones de pantalla
echo    • Videos exportados de editores
echo.
echo 3️⃣  Una vez que tengas archivos WEBM:
echo    • Usa la interfaz gráfica (opción 1)
echo    • O arrastra archivos a la ventana del programa
echo.
echo ⚠️  NOTA: Este programa convierte archivos reales,
echo     no puede crear archivos WEBM de prueba.
echo.
pause
goto menu

:command_line
echo.
echo 💻 MODO LÍNEA DE COMANDOS:
echo.
echo 🤓 Para usuarios avanzados que prefieren comandos:
echo.
echo 📝 SINTAXIS BÁSICA:
echo    python webm_to_mp4_converter.py archivo.webm
echo.
echo 📝 OPCIONES AVANZADAS:
echo    python webm_to_mp4_converter.py -f carpeta -q high
echo.
echo 🎯 ¿Quieres probar el modo comando?
set /p cmd_choice="(s/n): "
if /i "%cmd_choice%"=="s" (
    echo.
    echo 🚀 Abriendo menú interactivo de comandos...
    call ejemplos.bat
)
goto menu

:invalid
echo.
echo ❌ Opción inválida. Por favor selecciona 0-6.
timeout /t 2 >nul
goto menu

:exit
echo.
echo ════════════════════════════════════════════════
echo   🎊 ¡Gracias por probar el Conversor WEBM a MP4!
echo ════════════════════════════════════════════════
echo.
echo 💡 RECUERDA:
echo   • Usa iniciar_interfaz.bat para la interfaz gráfica
echo   • Revisa README.md para documentación completa
echo   • Ejecuta instalar.bat si tienes problemas
echo.
echo 🎬 ¡Disfruta convirtiendo tus videos! ✨
echo.
timeout /t 3 >nul
exit /b 0
