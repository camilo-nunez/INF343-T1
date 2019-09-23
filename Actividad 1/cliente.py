import socket
import logging

logging.basicConfig(level = logging.INFO, filename = 'respuestas.txt', filemode = 'w', format = '%(asctime)s - %(message)s')

# obtiene IP propia
host = "172.20.0.10"
port = 5000
BUFFER_SIZE = 1024
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect( (host, port) )

# manda el mensaje de solicitud al servidor
cliente.send(b"Esta es la peticion !")

# recibe la confirmacion
data = cliente.recv(BUFFER_SIZE)
logging.info(data)
print(data)

# cierre de socket
cliente.close()
