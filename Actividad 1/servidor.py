import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
import logging

logging.basicConfig(level = logging.INFO, filename = 'log.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

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
        
        self.conn.send(data  + " recibido.")
        
        cerrando = "Cerrando conexion."
        logging.info(cerrando)
        print(cerrando)

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
serverSocket.listen(100)
esperando = "Esperando clientes"
logging.info(esperando)
print(esperando)
i = 0

while True:
	
    (conn, (ip, port)) = serverSocket.accept()
    
    # se crea nuevo ServerThread 
    newServerThread = ServerThread(ip, port, conn)
    newServerThread.start()
    
    # esperar hasta que cada serverThread termine
    # newServerThread.join()
    threads.append(newServerThread)
    i += 1

serverSocket.close()

