import socket
import re
import base64

s = ('challenge02.root-me.org', 52023)

# conexion al nc

se = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
se.connect(s)

# recibir el mensaje y desencriptarlo

def base_64(msg):
    b64_string = re.search('(?<= is )(\S+)',msg)
    b64_string = b64_string.group()
    
    b64_string = b64_string.replace('\'', '')
    b64_string = b64_string.replace('.', '')
   
    base64_bytes = b64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    
    print(b64_string)
    send(sample_string.encode())

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
base_64(str_data)
