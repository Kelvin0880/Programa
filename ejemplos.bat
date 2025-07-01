@echo off
echo ========================================
echo     Conversor WEBM a MP4 - Ejemplos
echo ========================================
echo.

:menu
echo Selecciona una opción:
echo.
echo 1. Convertir un archivo específico
echo 2. Convertir todos los WEBM de una carpeta
echo 3. Convertir con calidad alta
echo 4. Mostrar ayuda del programa
echo 5. Salir
echo.
set /p choice="Ingresa tu opción (1-5): "

if "%choice%"=="1" goto single_file
if "%choice%"=="2" goto folder_conversion
if "%choice%"=="3" goto high_quality
if "%choice%"=="4" goto show_help
if "%choice%"=="5" goto exit
goto invalid

:single_file
echo.
set /p file_path="Ingresa la ruta completa del archivo WEBM: "
echo.
echo Convirtiendo archivo...
python webm_to_mp4_converter.py "%file_path%"
pause
goto menu

:folder_conversion
echo.
set /p folder_path="Ingresa la ruta de la carpeta con archivos WEBM: "
echo.
echo ¿Buscar en subcarpetas también? (s/n):
set /p recursive_choice=""
echo.
echo Convirtiendo archivos...
if /i "%recursive_choice%"=="s" (
    python webm_to_mp4_converter.py -f "%folder_path%" -r
) else (
    python webm_to_mp4_converter.py -f "%folder_path%"
)
pause
goto menu

:high_quality
echo.
set /p hq_path="Ingresa la ruta del archivo o carpeta: "
echo.
echo ¿Es una carpeta? (s/n):
set /p is_folder=""
echo.
echo Convirtiendo con calidad alta...
if /i "%is_folder%"=="s" (
    python webm_to_mp4_converter.py -f "%hq_path%" -q high
) else (
    python webm_to_mp4_converter.py "%hq_path%" -q high
)
pause
goto menu

:show_help
echo.
python webm_to_mp4_converter.py --help
echo.
pause
goto menu

:invalid
echo.
echo ❌ Opción inválida. Por favor selecciona 1-5.
echo.
pause
goto menu

:exit
echo.
echo ¡Hasta luego! 👋
exit /b 0
