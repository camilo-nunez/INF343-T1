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
        info = "Se crea ServerThread para cliente con IP " + ip + ":" + str(port)
        registro.info(info)
        print(info)
 
    def run(self):
        # Recibe el mensaje de conexion
        data = self.conn.recv(bufferSize).decode("utf-8")
        logging.info(data)
        print("Mensaje recibido: " + data)

        # Confirma la conexion
        self.conn.send(b"confirmacion")
        print("Se envia confirmacion")
		
		# Recibe mensajes
		while True:
			data = conn.recv(bufferSize).decode("utf-8")
			eleccionData = random.randInt(len(threads))
			
			while threads[eleccionData].getConn() != self.conn:
				
			print(data)
			logging.info(data)
        
        cerrando = "Cerrando conexion."
        logging.info(cerrando)
        print(cerrando)
        
    def getConn(self):
        return self.conn
		
# Servidor multithread
registro = loggingFactory("registro", "registro_server.txt")
hearbeat = loggingFactory("hearbeat", "hearbeat_server.txt")

bufferSize = 1024

IP = socket.gethostbyname(socket.gethostname()) 
PORT = 5000
BUFFER_SIZE = 1024  # cambiar en caso de que se quiera

# multicast
multicastGroup = "172.30.0.0"
multicastPort = 6000

multi = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

multi.settimeout(1)

ttl = struct.pack('b', 1)
multi.setsockpot(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL, ttl)


# Server Tipo TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket de Servidor iniciado.")

#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.bind((IP, PORT))

threadsMensajes = list()

socketsAndMensajes = dict()

# se aceptan 100 conexiones simultaneas
serverSocket.listen(3)
esperando = "Esperando dataNodes"
registro.info(esperando)
print(esperando)

def heartbeat():
	sent = multi.sendto("hearbeat", multicastGroup)
	dataNodes = []
	
	while True:
		try:
			data, server = sock.recvfrom(16) # ver que es el 16
			dataNodes.append(server)
		except socket.timeout:
			print("timeout")
		else:
			hearbeat.info(data + " de " + data + " " + server + "no disponible")
			
	for i in range(len(threads)):
		ip = dataNodes[i].split(":")[0]
		
		if not ip in dataNodes:
			hearbeat.info(data + " de " + data + " " + server + "no disponible")
			
hearbeatTimer = Timer(5, heartbeat)
hearbeatTimer.start()

while True :
    (conn, (ip, port)) = serverSocket.accept()
    
    # se crea nuevo ServerThread 
    newServerThread = ServerThread(ip, port, conn)
    newServerThread.start()
    
    threads.append(newServerThread)

# serverSocket.close()

