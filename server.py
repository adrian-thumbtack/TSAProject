import socket
from empath import Empath

def handler(conn):
	conn.send(bytearray("HTTP/1.1 200 OK\n","utf-8"))
	conn.send(bytearray("Content-Type: text/html\n\n","utf-8"))
	text = "HH SPED" #do this from twitter and scheisse
	d = Empath().analyze(text)
	depressed = d["sadness"] > d["joy"] #bs af
	f = open("depression.html",'r')
	conn.send(bytearray(f.read(),"utf-8"))
	f.close()
	conn.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('',80))
serv.listen(65)
while True:
	conn,_ = serv.accept()
	handler(conn)
serv.close()
