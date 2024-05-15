import socket
#Creates and connects the socket for the client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5969))
#Runs constantly to send and recieve messages from the server
while True:
    msg = input("Enter message: ")
    s.send(bytes(msg, "utf-8"))
    
    inc = s.recv(1024).decode("utf-8")
    print(inc)
    #if the server sent back the reversed "end", close the socket and the client
    if(inc == "dne"):
        s.close()
        break