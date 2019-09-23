import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
import logging

logging.basicConfig(level = logging.INFO, filename = 'log.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# ServerThread: servidor con PoolThread para multiples clientes
class ServerThread(Thread): 
 
    def __init__(self, ip, port):
		
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        info = "Se crea ServerThread para cliente con " + ip + ":" + str(port)
        logging.info(info)
        print(info)
 
    def run(self):
        
        # Recibe la conexion
        data = conn.recv(1024).decode("utf-8")
        logging.info(data)
        print("Mensaje recibido: " + data)

        # Confirma la conexion
        conn.send('Confirmo la conexion')

		# # Recibe mensaje 1
        # data = conn.recv(1024).decode("utf-8")
        # logging.info(data)
        # print (data)

		# # Recive mensaje
        # data = conn.recv(1024).decode("utf-8")
        # logging.info(data)
        # print (data)
        
        logging.info("Cerrando conexion.")
        print("Cerrando conexion.")


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

# se aceptan 4 conexiones simultaneas
serverSocket.listen(100)
esperando = "Esperando clientes"
logging.info(esperando)
print(esperando)

while True:
	
    (conn, (ip, port)) = serverSocket.accept()
    
    # se crea nuevo ServerThread 
    newServerThread = ServerThread(ip, port)
    newServerThread.start()
    
    # esperar hasta que cada serverThread termine
    newServerThread.join()
    threads.append(newServerThread)

serverSocket.close()
