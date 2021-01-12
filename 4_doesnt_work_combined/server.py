import socket
import time
import pickle
from ntru import *

HEADERSIZE = 10

q = 122430513841
f = 231231
g = 195698

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

con, addr = s.accept()
print("Connected to ", addr)

while True:
    msg = input("Send message to client: ") # input str
    enc = encrypt_message(msg, q, f, g) # inputs str, returns int array
    sendthis = pickle.dumps(d)
    sendthis = bytes(f"{len(enc):<{HEADERSIZE}}", 'utf-8')+enc
    con.send(enc) # gotta send int array

    print("Waiting for reply...")
    recieved_msg = con.recv(1024)
    dec = decrypt_message(recieved_msg.decode(), q, f, g)
    print("Client message: ", dec)