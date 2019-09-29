import socket 
from threading import Thread, Timer
from socketserver import ThreadingMixIn
import logging

def loggingFactory(nombre, archivo, tipo = logging.INFO):
	handler = logging.FileHandler(archivo)
	formato = logging.Formatter('%(asctime)s - %(message)s')
	handler.setFormatter(formato)
	
	logger = logging.getLogger(nombre)
	logger.setLevel(tipo)
	logger.addHandler(handler)
	
	return logger

registro = loggingFactory("registro", "registro_server.txt")
hearbeat = loggingFactory("hearbeat", "hearbeat_server.txt")
# logging.basicConfig(level = logging.INFO, filename = 'registro_server.txt', filemode = 'w', format = '%(asctime)s - %(message)s')
# logging.basicConfig(level = logging.INFO, filename = 'hearbeat_server.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

bufferSize = 1024
# ServerThread: servidor con PoolThread para multiples clientes
class ServerThread(Thread): 
 
    def __init__(self, ip, port, conn):
		
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        # registra nuevo SeverThread en log.txt
        info = "Se crea ServerThread para cliente con IP " + ip + ":" + str(port)
        logging.info(info)
        print(info)
 
    def run(self):
        
        # Recibe el mensaje de conexion
        data = self.conn.recv(bufferSize).decode("utf-8")
        logging.info(data)
        print("Mensaje recibido: " + data)

        # Confirma la conexion
        self.conn.send(b"confirmacion")
        print("Se envia confirmacion")
		
		# Recibe mensaje 1
        data = conn.recv(bufferSize).decode("utf-8")
        logging.info(data)
        print(data)
        
        cerrando = "Cerrando conexion."
        logging.info(cerrando)
        print(cerrando)
        
    def getConn(self):
        return self.conn
		
# Servidor multithread

IP = socket.gethostbyname(socket.gethostname()) 
PORT = 5000
BUFFER_SIZE = 1024  # cambiar en caso de que se quiera

# Server Tipo TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket de Servidor iniciado.")
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.bind((IP, PORT))

threads = list()

# se aceptan 100 conexiones simultaneas
serverSocket.listen(4)
esperando = "Esperando clientes"
logging.info(esperando)
print(esperando)
i = 0

def heartbeat():
	for i in range(len(threads)):
		data = threads[i].getConn.recv(BUFFER_SIZE).decode("utf-8")
		if data == "ok":
			hearbeat.info("thread " + str(i) + " esta vivo")
		else:
			hearbeat.info("thread " + str(i) + " no disponible")

hearbeatTimer = Timer(5, heartbeat)
hearbeatTimer.start()

while i < 4 :
	
    (conn, (ip, port)) = serverSocket.accept()
    
    # se crea nuevo ServerThread 
    newServerThread = ServerThread(ip, port, conn)
    newServerThread.start()
    
    threads.append(newServerThread)
    i += 1

serverSocket.close()

