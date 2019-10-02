import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
import logging

# se crea log.txt
logging.basicConfig(level = logging.INFO, filename = '/servidor/log.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

bufferSize = 1024

# ServerThread: servidor multiThread para multiples clientes
class ServerThread(Thread): 
 
    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port
        self.conn = conn
        
        # registra nuevo SeverThread en log.txt
        info = "Se crea ServerThread para cliente con IP " + ip + " : " + str(port)
        logging.info(info)
        print(info)
 
    def run(self):
        
        # Recibe peticion de conexion
        data = self.conn.recv(bufferSize).decode("utf-8")
        logging.info(data)
        print("Mensaje recibido: " + data)

        # Confirma la conexion
        self.conn.send(b"confirmacion, por favor veo los logs")
        
        # se reciben mensajes hasta que se reciba exit
        while True:
            # Recibe mensaje
            data = conn.recv(bufferSize).decode("utf-8")
            logging.info(data)
            self.conn.send(data.encode("utf-8"))

# variables
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 5000
BUFFER_SIZE = 1024  # cambiar en caso de que se quiera
threads = list()
i = 0

# Server Tipo TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket de Servidor iniciado.")
serverSocket.bind( (IP, PORT) )

# se aceptan 100 conexiones simultaneas
serverSocket.listen(100)
esperando = "Esperando clientes"
logging.info(esperando)
print(esperando)

while i < 100:
    (conn, (ip, port)) = serverSocket.accept()
    
    # se crea nuevo ServerThread 
    newServerThread = ServerThread(ip, port, conn)
    newServerThread.start()
    
    # esperar hasta que cada serverThread termine
    threads.append(newServerThread)
    i += 1

# se cierra servidor despues de 100 clientes
serverSocket.close()

