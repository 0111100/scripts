import socket
import re
from math import sqrt

s = ('challenge01.root-me.org', 52002)

# conexion al nc 

se = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
se.connect(s)


# calculo de la raiz cuadrada + multiplicación

def math_calc(msg):
	valor1 = re.search('(?<=root of )(\w+)',msg)
	valor1 = valor1.group()
	
	valor2 = re.search('(?<=multiply by )(\w+)',msg)
	valor2 = valor2.group()

	square = int(valor1)
	multi = sqrt(square) * int(valor2)
	multi = round(multi,2)
	multi = str(multi).encode()
	send(multi)
	print(multi)

# declarar la funcion send

def send(msg):
    se.sendall(msg)
    se.shutdown(socket.SHUT_WR)
    while 1:
        data = se.recv(1024)
        if len(data) == 0:
            break
        print("Received:", repr(data))
    print("Connection closed.")
    se.close()

# declarar formato del textp recibido

data = se.recv(10240)
str_data = str(data, 'UTF-8')
math_calc(str_data)	


