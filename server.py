import socket

def handler(conn):
	conn.send("HTTP/1.1 200 OK\n")
	conn.send("Content-Type: text/html\n\n")
	f = open("depression.html",'r')
	conn.send(f.read())
	f.close()
	conn.close()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('',80))
serv.listen(65)
while True:
	conn,_ = serv.accept()
	handler(conn)
serv.close()
