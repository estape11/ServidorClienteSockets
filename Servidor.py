"""
********************************************************************* 

Instituto Tecnológico de Costa Rica 

    Ingeniería en Computadores

 Lenguaje: Python 3.6.1

 Autor: Esteban Agüero Pérez

 Versión: 1.0

 Fecha Última Modificación: Octubre 24/2017

 Ejemplo de servidor multi threading por sockets.

***********************************************************************
"""

import socket
import sys
import threading

def Conexion(connection,client_address):
    try:
        while True:
            data = connection.recv(1024) #se define cuantos bytes se reciben
            if data:
                mensaje=data.decode()
                print("Dato recibido de",client_address, ": %s" % mensaje)
                respuesta="--Mensaje Recibido--"
                connection.send(bytes(respuesta,"utf-8"))
                #Aqui se puede agregar las respuestas o lo que se quiere hacer con los resultados recibidos
                if mensaje=="exit":
                    connection.close()
    except:
        connection.close()

def Iniciar(ip,puerto):
    # Creando el socket TCP/IP (protocolo de comunicacion)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enlace de socket y puerto
    server_address = (ip, puerto) #Se puede cambiar el IP
    print('Abriendo IP %s Puerto %s' % server_address)
    sock.bind(server_address)
    sock.listen(1)
    listaConexiones =[] #almacena las conexiones
    hilosConexiones=[] #almacena los hilos de las conexiones (escucha)
    while True:
        # Esperando conexion
        print ('Esperando conexión...')
        connection, client_address = sock.accept()

        try:
            print ('Nuevo cliente, conectado desde', client_address)
            listaConexiones.append(connection)
            try:
                #Por cada cliente crea un 
               t=threading.Thread(target=Conexion, args=(connection,client_address,))
               hilosConexiones.append(t)
               t.start()
            except:
               print ("Error: no se pudo iniciar el hilo") 
        except:
           sock.close()
           
Iniciar("localhost",8080)
