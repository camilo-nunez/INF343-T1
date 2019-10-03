from threading import Thread
import socket
import logging
from socketserver import ThreadingMixIn
import struct

# crea archivos registro a partir de la clase logging
def loggingFactory(nombre, archivo, tipo = logging.INFO):
    handler = logging.FileHandler(archivo)
    formato = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formato)
    
    logger = logging.getLogger(nombre)
    logger.setLevel(tipo)
    logger.addHandler(handler)

    return logger

# registros
registroData = loggingFactory("data", "/dataNode/data.txt")

# recibe mensajes
class ReceiveThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            # mensaje a guardar
            data = dataNode.recv(bufferSize).decode("utf-8")

            # se registra en data.txt
            registroData.info(data)
            
            # avisa que fue recibido
            dataNode.send(b"recibido")

# variables
host = "172.30.0.10"
port = 5000
bufferSize = 1024

# socket mensajes
dataNode = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dataNode.connect( (host, port) )

registroData.info('Conexion establecida con ' + str(dataNode.getsockname()) + ' y ' + str(dataNode.getpeername()))


# handshake 3 pasos
dataNode.send(b"peticion")
data = dataNode.recv(bufferSize).decode("utf-8")

if data != "confirmacion":
    registroData.info("Servidor no conecta.")
    dataNode.close()
    exit(0)

registroData.info(data)
dataNode.send(b"dataNode")

# entrada para el usuario
receiveThread = ReceiveThread()
receiveThread.start()

# dataNode.close()
