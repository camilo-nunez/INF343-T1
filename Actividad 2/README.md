# Actividad 2

* Se usaron los containers de python:latest.
* Se instaló nano para ver los archivos creados.
* IP del servidor: *172.30.0.10*
* Puerto para multicast: *6000*
* Dirección de multicast: *224.1.1.1*
* Directorio de todos los registros: */*
* Para ver los archivos:
    * opción: ```tail -f {registro_server.txt,hearbeat_server.txt,dataNode.txt,registro_cliente.txt}```

Para ejecutar:

* **$** ```sudo docker-compose build```
* **$** ```sudo docker-compose up```
