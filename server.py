from socket import *
import os
s= socket()
print("socket successfully created")

def req_file(path):
	sp=path.split()
	if sp[2][:4]=="HTTP":
		if os.path.isfile(sp[1]): 
			f=open(sp[1])
			a = f.read()
			ans=""
			ans+="200 OK\n"
			if sp[1][-2:]=="xt" or sp[1][-2:]=="ml":
				ans+="Content-Type : text/html\n"
			else:
				ans+="Content-Type : image\n"
			if sp[2][-1]=="0":
				ans+="Connection : Close\n"
			else:
				ans+="Connection : Keep-Alive\n"
			ans+=a
			return ans
		else:
			print("404 Not Found")
	else:
		print("403 Forbidden")	


s.bind(('', 2006))
s.listen(5)
print("socket is listening")
while True:
	addr='127.0.0.1'
	c,addr=s.accept()
	print("got connection from" , addr)
	req=c.recv(1024)
	r_f=req_file(req)
	c.send(r_f)
	c.close()

