import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn
import logging

logging.basicConfig(level=logging.INFO, filename='log.txt', filemode='w', format='%(asctime)s - %(message)s')

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        logging.info("[+] New server socket thread started for " + ip + ":" + str(port))
        print ("[+] New server socket thread started for " + ip + ":" + str(port))
 
    def run(self):
        
        # Recive la conexion
        data = conn.recv(2048).decode("utf-8")
        logging.info(data)
        print (data)

        # Confirma la conexion
        conn.send('Confirmo la conexion')

		# # Recive mensaje 1
        # data = conn.recv(2048).decode("utf-8")
        # logging.info(data)
        # print (data)

		# # Recive mensaje
        # data = conn.recv(2048).decode("utf-8")
        # logging.info(data)
        # print (data)
        
        logging.info("[+] Close conection client.")
        print("[+] Close conection client.")


# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = socket.gethostbyname(socket.gethostname()) 
TCP_PORT = 5000
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 


while True: 
    tcpServer.listen(4) 
    logging.info("Multithreaded Python server : Waiting for connections from TCP clients...")
    print("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 