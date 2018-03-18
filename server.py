import socket
from empath import Empath

filesToSend = {
	b"style.css":b"css",
	b"media/header.jpg":b"jpeg"
}
defaultFile = [b"depression.html",b"html"]
def sendFile(conn,filename,type):
	conn.send(type)
	conn.send(b"\n\n")
	f = open(filename,"rb")
	conn.send(f.read())
	f.close()
def handler(conn):
	data = conn.recv(1024)
	conn.send(b"HTTP/1.1 200 OK\nContent-type: text/")
	sentSomething = False
	for filename,type in filesToSend.items():
		if data.find(filename) != -1:
			sendFile(conn,filename,type)
			sentSomething = True
	if not sentSomething:
		sendFile(conn,defaultFile[0],defaultFile[1])
	conn.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("",80))
serv.listen(65)
processes = []
while True:
	conn,_ = serv.accept()
	handler(conn)
serv.close()
