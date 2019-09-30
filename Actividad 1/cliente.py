import socket
import logging

logging.basicConfig(level = logging.INFO, filename = 'respuestas.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# IP servidor
host = "172.20.0.10"
port = 5000
bufferSize = 1024
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect( (host, port) )

# manda el mensaje de solicitud al servidor
cliente.send(b"peticion")

# recibe la confirmacion
data = cliente.recv(bufferSize).decode("utf-8")
logging.info(data)
print(data)

# mensaje 1
cliente.send(b"saludos")
print("Se envió mensaje 1.")

while data != "cerrando conexion":
	data = cliente.recv(bufferSize).decode("utf-8")
	cliente.info("se recibio:" + data)

cliente.info("adios")
