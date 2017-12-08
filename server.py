from socket import *
import os
import time
s= socket()
print("socket successfully created")

def req_file(path):
	sp=path.split()
	print(sp)
	if  sp[2][:4]=="HTTP":
		if os.path.isfile(sp[1]): 
			f=open(sp[1])
			a=f.read()
			ans=""
			ans+="HTTP/1.1 200 OK\r\n"
			if sp[1][-2:]=="xt" or sp[1][-2:]=="ml":
				ans+="Content-Type : text/html\r\n"
			else:
				ans+="Content-Type : image\r\n"
			ans+="Content-Length : "+ str(len(a))+ "\r\n"
			if sp[2][-1]=="0":
				ans+="Connection : Close\r\n\r\n"
			else:
				ans+="Connection : Keep-Alive\r\n\r\n"
			return ans
		else:
			return "HTTP/1.1 404 Not Found\r\n\r\n"
	else:
		return "HTTP/1.1 403 Forbidden\r\n\r\n"

def content(path):
	sp=path.split()
	if os.path.isfile(sp[1]): 
		f=open(sp[1])
		a=f.read()
		return a 
	else:
		return "HTTP/1.1 404 Not Found\r\n\r\n"

s.bind(('127.0.0.1', 8080))
s.listen(5)
print("socket is listening")
while True:
	addr='127.0.0.1'
	c,addr=s.accept()
	print("got connection from" , addr)
	req=c.recv(1000)
	pid=os.fork()
	if pid==0:
		time.sleep(5)
		r_f=req_file(req)
		con=content(req)
		c.send(r_f)
		c.send(con)
		c.close()
	else:
		c.close()

