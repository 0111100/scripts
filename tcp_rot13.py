import socket
import re
import codecs

s = ('challenge01.root-me.org', 52021)

# conexion al nc

se = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
se.connect(s)

def rot13(msg):
    valor = re.search('(?<= is )(\S+)',msg)
    valor = valor.group()
    
    valor = valor.replace('\'', '')
    valor = valor.replace('.', '')

    valor = codecs.decode(valor, 'rot_13')
    print(valor)
    send(valor.encode())
#

def send(msg):
    se.sendall(msg)
    se.shutdown(socket.SHUT_WR)
    while 1:
        data = se.recv(10240)
        if len(data) == 0:
            break
        print("Received:", repr(data))
    print("Connection closed.")
    se.close()

# declarar formato del texto recibido

data = se.recv(10240)
str_data = str(data, 'UTF-8')
print(str_data)
rot13(str_data)
