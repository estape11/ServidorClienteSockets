"""
********************************************************************* 

Instituto Tecnológico de Costa Rica 

    Ingeniería en Computadores

 Lenguaje: Python 3.6.1

 Autor: Esteban Agüero Pérez

 Versión: 1.0

 Fecha Última Modificación: Octubre 24/2017

 Ejemplo de cliente por sockets.

***********************************************************************
"""


import socket
import sys
import threading

#Funcion para escuchar desde el servidor
def Escuchar(servidor):
    try:
         while True:
            data = servidor.recv(1024) #se define cuantos bytes se reciben
            if data:
                mensaje=data.decode()
                print("Dato recibido de: %s" % mensaje,"\n")
    except:
        servidor.close()

def ConectarServidor(ip,puerto):
    # Creando un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta el socket en el puerto cuando el servidor esté escuchando
    server_address = (ip, puerto)
    print ('Conectando a IP %s Puerto %s' % server_address)
    sock.connect(server_address)

    try:
        hiloServidor=threading.Thread(target=Escuchar, args=(sock,))
        hiloServidor.start()
    except:
               print ("Error: no se pudo iniciar el hilo")

    #Enviando datos
    try:
        while True:
            men=input("Mensaje: ")
            sock.send(bytes(men,"utf-8"))
    except:
        print ('Conexion perdida, cerrando socket')
        sock.close()
        
ConectarServidor("localhost",8080)
