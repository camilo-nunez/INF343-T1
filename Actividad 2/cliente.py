import socket
import logging
import random
from threading import Timer

# se crea registro_cliente.txt
logging.basicConfig(level = logging.INFO, filename = '/cliente/registro_cliente.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# IP servidor
host = "172.30.0.10"
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
cliente.send(b"cliente")

# se envian como mensajes numeros random
def randomMSG():
    Timer(0.5, randomMSG).start()
    numero = random.randint(0, 100)
    msg = "numero random: " + str(numero)
    cliente.send(msg.encode("utf-8"))

    # espera a que su mensaje sea distribuido
    data = cliente.recv(bufferSize).decode("utf-8")
    logging.info(data)

randomMSG()
