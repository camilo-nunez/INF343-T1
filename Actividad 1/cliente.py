# Python TCP Client A
import socket 

#host = socket.gethostname()
host = "10.6.43.83"
port = 1234
BUFFER_SIZE = 2000 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

# Manda el mensaje de solicitud al servidor
tcpClientA.send(b"Esta es la peticion !")

# Recive la confirmación
data = tcpClientA.recv(BUFFER_SIZE)
print(data)


# Manda el mensaje 1
tcpClientA.send(b"Mensaje 1")

# Manda el mensaje 2
tcpClientA.send(b"Mensaje 2")

tcpClientA.close()