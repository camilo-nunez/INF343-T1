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
# registroData = loggingFactory("data", "/dataNode/dataNode_"+socket.gethostbyname(socket.gethostname())+".txt")
registroData = loggingFactory("data", "/dataNode/dataNode.txt")

# thread que respondera a los hearbeat del headNode
"""class HeartThread(Thread): 
 
    def __init__(self):
        Thread.__init__(self)

        heart = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        heart.bind( ('', heartPort) )
        grupo = socket.inet_aton(heartAddress)
        mreq = struct.pack('4sL', grupo, socket.INADDR_ANY)
        heart.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def run(self):
        while True:
            data, direccion = heart.recvfrom(1024)
            
            if data.decode("utf-8") == "hearbeat":
                heart.sendto(b"ok", direccion)
"""
# recibe mensajes
class ReceiveThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            # mensaje de otro
            data = dataNode.recv(bufferSize).decode("utf-8")
            
            # si es data de otro
            if data.split(" ")[0] == "another":
                registroData.info(data.split(" ", 1)[1])
                registroData.info("recibido")
                dataNode.send(b"recibido")
            # si es donde quedo la data enviada por este
            else:
                registroData.info(data)
                registroData.info("registrado")
                dataNode.send(b"registrado")

# variables
host = "172.30.0.10"
port = 5000
bufferSize = 1024

# socket mensajes
dataNode = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dataNode.connect( (host, port) )

# handshake 3 pasos
dataNode.send(b"peticion")
data = dataNode.recv(bufferSize).decode("utf-8")

if data != "confirmacion":
    registroData.info("Servidor no conecta.")
    data.close()
    exit(0)

# registrodata.info(data)
dataNode.send(b"dataNode")

# entrada para el usuario
receiveThread = ReceiveThread()
receiveThread.start()

# dataNode.close()
