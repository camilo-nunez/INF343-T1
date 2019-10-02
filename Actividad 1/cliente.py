import socket
import logging
import random
from threading import Timer
# se crea respuestas.txt
logging.basicConfig(level = logging.INFO, filename = '/cliente/respuestas.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# IP servidor
host = "172.20.0.10"
port = 5000
bufferSize = 1024
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect( (host, port) )

# manda el mensaje de solicitud al servidor
cliente.send(b"peticion")

# recibe la confirmacion
data = cliente.recv(bufferSize).decode("utf-8")
logging.info(data)
print(data)

# se envian como mensajes numeros random
def randomMSG():
    Timer(3.0, randomMSG).start()
    numero = random.randint(0, 100)
    msg = "numero random: " + str(numero)
    cliente.send(msg.encode("utf-8"))

    data = cliente.recv(bufferSize).decode("utf-8")
    logging.info("Servidor recibio: " + data)

randomMSG()
