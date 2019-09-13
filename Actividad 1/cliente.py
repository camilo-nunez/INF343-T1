# Python TCP Client A
import socket 
import logging

logging.basicConfig(level=logging.INFO, filename='respuestas.txt', filemode='w', format='%(asctime)s - %(message)s')

#host = socket.gethostname()
host = socket.gethostbyname(socket.gethostname())
port = 5000
BUFFER_SIZE = 2000 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

# Manda el mensaje de solicitud al servidor
tcpClientA.send(b"Esta es la peticion !")

# Recive la confirmacion
data = tcpClientA.recv(BUFFER_SIZE)
logging.info(data)
print(data)

# # Manda el mensaje 1
# tcpClientA.send(b"Mensaje 1")

# # Manda el mensaje 2
# tcpClientA.send(b"Mensaje 2")

tcpClientA.close()