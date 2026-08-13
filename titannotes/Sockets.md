
#!/bin/python3


import socket 

HOST = "127.0.0.1"
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

run command nc -nvlp 7777
		to get these - listening on [any] 7777 . 
