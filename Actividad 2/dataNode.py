import socket
import logging

logging.basicConfig(level = logging.INFO, filename = 'registro_cliente.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# obtiene IP propia
host = "172.30.0.10"
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
cliente.send(b"mensaje 1")
print("Se envió mensaje 1.")

print("Cerrando cliente...")

# cierre de socket
cliente.close()
