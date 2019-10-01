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

# thread que respondera a los hearbeat del headNode
class HeartThread(Thread): 
 
    def __init__(self):
        
        Thread.__init__(self)

        heart = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        heart.bind( ("", 6000) )
        group = socket.inet_aton(host)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        heart.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def run(self):
        while True:
            data, direccion = heart.recvfrom(1024)
            if data == "hearbeat":
                heart.sendto("ok", direccion)
                
class ReceiveThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):

        while True:
            data = dataNode.recv(bufferSize).decode("utf-8")
            registroData.info()
            dataNode.send(b"recibido")
          

# registros
registroCliente = loggingFactory("registroCliente", "registro_cliente.txt")
registroData = loggingFactory("data", "data.txt")

# variables
host = "172.30.0.10"
port = 5000
heartPort = 6000
bufferSize = 1024
dataNode = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dataNode.connect( (host, port) )

# handshake 3 pasos
dataNode.send(b"peticion")
data = dataNode.recv(bufferSize).decode("utf-8")

if data != "confirmacion":
    print("servidor no conecta")
    cliente.close()
    exit(0)

dataNode.send(b"ok")

# entrada para el usuario
receiveThread = ReceiveThread()
receiveThread.start()

# responder al hearbeat
heartThread = HeartThread()
heartThread.start()

# recibe mensajes del dataNode
while True :
    
    print("Ingresar mensaje: ")
    data = input()
    
    if data == "exit":
        break

    # envia
    dataNode.send(data.encode("utf-8"))
    print("Se envió mensaje.")

dataNode.close()
