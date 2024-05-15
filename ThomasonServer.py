from pickle import NONE
import select
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5969))
s.listen(5)
def reverse(msg):
    i = 0;
    revd = ""
    length = len(msg)
    while i < length:
        revd = revd + msg[(length-i)-1]
        i+=1
        
    return revd
while True:
    clientsocket, address = s.accept()
    print(f"Connected to {address}")
    while clientsocket != NONE:
        msg = clientsocket.recv(1024).decode("utf-8")
        clientsocket.send(bytes(reverse(msg), "utf-8"))
        if(msg == "end"):
            clientsocket.close()
            clientsocket = NONE
    


