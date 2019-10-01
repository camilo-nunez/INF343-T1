import socket 
from threading import Thread, Timer
from socketserver import ThreadingMixIn
import logging
import random
import struct
import sys

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
        
        # registra nuevo SeverThread en registro_server.txt
        inicio = "Se crea ServerThread para cliente con IP " + ip + " puerto " + str(port)
        registro.info(inicio)
        print(inicio)
 		
    def run(self):
		
        # handshake 3 pasos
        data = self.conn.recv(bufferSize).decode("utf-8")
        logging.info(data)
        print("Mensaje recibido: " + data)

        self.conn.send(b"confirmacion")
        print("Se envia confirmacion")
		
        data = self.conn.recv(bufferSize).decode("utf-8")

        if data == "ok":
            
            # Recibe mensajes
            while True:
                data = self.conn.recv(bufferSize).decode("utf-8")

                eleccionData = random.randint(0, len(threads))

                while threads[eleccionData].getConn() == self.conn:
                    eleccionData = random.randint(0, len(threads))

                nodeAndData = str(threads[eleccionData].getConn()) + " " + data
                threads[eleccionData].getConn().send(nodeAndData.encode("utf-8"))

                print("Mensaje ya distribuido: " + data)
                registro.info(str(threads[eleccionData].getIP()) + data)

                # respuesta si se recibio
                data = threads[eleccionData].getConn().recv(bufferSize).decode("utf-8")

                if data == "recibido":
                    registro.info("registro de data:" + data + " - realizado correctamente") 
			
    def getConn(self):
        return self.conn
        
    def getIP(self):
        return self.IP

# registros
registro = loggingFactory("registro", "registro_server.txt")
hearbeat = loggingFactory("hearbeat", "hearbeat_server.txt")

# variables
bufferSize = 1024
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 5000
threads = list()
socketsAndMensajes = dict()

# multicast
multicastGroup = "172.30.0.0"
multicastPort = 6000

multi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
multi.bind(('', multicastPort))
multi.settimeout(1)
ttl = struct.pack('b', 1)
multi.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Server Tipo TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket de Servidor iniciado.")

#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.bind((IP, PORT))

# se aceptan 100 conexiones simultaneas
serverSocket.listen(100)
esperando = "Esperando dataNodes"
registro.info(esperando)
print(esperando)

def heartbeat():
    h = b"heartbeat"
    sent = multi.sendto((h, multicastGroup))
    dataNodes = []
	
    while True:
        try:
            data, server = sock.recvfrom(1024)
            if data == "ok":
                dataNodes.append(server[0])
			
        except socket.timeout:
            break

    for i in range(len(threads)):
        if not dataNodes[i] in dataNodes:
            hearbeat.info("data: " + data + " de " + server + "no disponible")
        else:
            hearbeat.info("data: " + data + " de " + server + "disponible")

hearbeatTimer = Timer(5, heartbeat)
hearbeatTimer.start()

# se esperan dataNodes
while True :
    (conn, (ip, port)) = serverSocket.accept()
    
    # se crea nuevo ServerThread 
    newServerThread = ServerThread(ip, port, conn)
    newServerThread.start()

    threads.append(newServerThread)
