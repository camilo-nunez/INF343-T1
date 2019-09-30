from threading import Thread
import socket
import logging
from socketserver import ThreadingMixIn

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
 
    def __init__(self, ip, port, conn):
		
        Thread.__init__(self)
        self.ip = ip 
        self.port = port
        self.conn = conn
        # registra nuevo SeverThread en log.txt
        info = "Se crea ServerThread para cliente con IP " + ip + ":" + str(port)
        logging.info(info)
        print(info)
        heart = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        heart.bind( (IP, port) )
        heart.listen(1)
        (conn, (ip, port)) = heart.accept()
	def run(self):
		
		while True:
			
			data = heart.recv(bufferSize).decode("utf-8")
			
			if data == "hearbeat":
			    heart.send("ok")
			else:
				cliente.send("not ok")

# registros
registroCliente = logging("registroCliente", "registro_cliente.txt")
registroData = logging("data", "data.txt")

# IP del headNode
host = "172.30.0.10"
port = 5000
heartPort = 6000
bufferSize = 1024
headNode = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
headNode.connect( (host, port) )

# manda el mensaje de solicitud al servidor
cliente.send(b"peticion")

while True:
	
	# mensaje 1
	cliente.send(b"mensaje 1")
	print("Se envió mensaje 1.")

	print("Cerrando cliente...")

# cierre de socket
cliente.close()
