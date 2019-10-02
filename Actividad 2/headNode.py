import socket 
from threading import Thread, Timer
from socketserver import ThreadingMixIn
import logging
import random
import struct
import sys
import os

# crea archivos registro a partir de la clase logging
def loggingFactory(nombre, archivo, tipo = logging.INFO):
    handler = logging.FileHandler(archivo)
    formato = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formato)
    
    logger = logging.getLogger(nombre)
    logger.setLevel(tipo)
    logger.addHandler(handler)
    
    return logger

# ServerThread: servidor con PoolThread para multiples clientes
class ServerThread(Thread): 
 
    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        
    def run(self):

        while True:
            data = self.conn.recv(bufferSize).decode("utf-8")

            eleccionData = random.randint(0, len(threads))

            while threads[eleccionData].getConn() == self.conn:
                eleccionData = random.randint(0, len(threads))

            nodeAndData = "another" + str(threads[eleccionData].getConn()) + " " + data
            
            # se distribuye
            threads[eleccionData].getConn().send(nodeAndData.encode("utf-8"))

            registro.info(str(threads[eleccionData].getIP()) + ":" + data)
            
            data = threads[eleccionData].getConn().recv(bufferSize).decode("utf-8")

            # se informa
            if data == "recibido":
                registro.info("registro de data:" + data + " - realizado correctamente")
                msg = data + " distribuido en " + threads[eleccionData].getIP()
                self.conn.send(msg.encode("utf-8"))
                data = self.conn.recv(bufferSize).decode("utf-8")
                if data == "registrado":
                    registro.info("registrado en origen")
            
    def getConn(self):
        return self.conn
        
    def getIP(self):
        return self.ip
        
class ClientThread(Thread): 
 
    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
    
    def run(self):
        while True:
            data = self.conn.recv(bufferSize).decode("utf-8")
    
    def getConn(self):
        return self.conn
        
    def getIP(self):
        return self.ip
        
# registros
registro = loggingFactory("registro", "registro_server.txt")
hearbeat = loggingFactory("hearbeat", "hearbeat_server.txt")

# variables
bufferSize = 1024
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 5000
threads = list()

# Server Tipo TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket de Servidor iniciado.")

serverSocket.bind((IP, PORT))

# se aceptan 100 conexiones simultaneas
serverSocket.listen(100)
esperando = "Esperando dataNodes"
registro.info(esperando)

# heartbeat
def heartbeat():
    Timer(5.0, heartbeat).start()
    
    for i in range(len(threads)):
        estado = os.system("ping -c 1 " + threads[i].getIP())
        
        if estado == 0:
          hearbeat.info(threads[i].getIP() + " disponible")
        else:
          hearbeat.info(threads[i].getIP() + " no disponible, eliminado")
          threads.remove(threads[i])
    
    if len(threads) == 0:
        registro.info("no hay dataNodes")

# thread de hearbeat cada 5 seg
heartbeat()

# se esperan 3 dataNodes, ultimo thread de cliente
while True :
    (conn, (ip, port)) = serverSocket.accept()
    
    inicio = "Se crea ServerThread para cliente con IP " + ip + " puerto " + str(port)
    registro.info(inicio)
    
    # handshake 3 pasos
    data = conn.recv(bufferSize).decode("utf-8")
    registro.info(data)

    conn.send(b"confirmacion")
    
    data = conn.recv(bufferSize).decode("utf-8")
    
    # se crea nuevo ServerThread
    if data == "dataNode":
        newServerThread = ServerThread(ip, port, conn)
        threads.append(newServerThread)
        newServerThread.start()
        
    elif data == "cliente":
        ClientThread(ip, port, conn).start()
