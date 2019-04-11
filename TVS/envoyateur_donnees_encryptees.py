from Crypto.Cipher import AES
import base64
import socket
import sys
 
def addPad(s): 
	return s + ((AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)).encode()
 
def encrypt(data, key, iv):
    return AES.new(key=key, mode=AES.MODE_CBC, IV=iv).encrypt(addPad(data))
    
def decrypt(data, key, iv):
    return AES.new(key=key, mode=AES.MODE_CBC, IV=iv).decrypt(data)


def sendFile(filename, serverAddress, serverPort):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((serverAddress, serverPort))
	print("Sending file...")
	
	with open(filename, "rb") as f:
		bytes = f.read()
		bytes = encrypt(bytes, b'\x41'*16, b'\x42'*16)
		s.sendall(bytes)
	s.close()
	
def streaming(localPort, serverAddress, serverPort, key, iv):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Listening at port {}".format(localPort))
	try:
		server.bind("localhost", localPort)
	except:
		print ("Unable to listen on the Port" + localPort)
		sys.exit()
	
	server.listen()
	local_socket = server.accept()
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((serverAddress, serverPort))

	local_socket.settimeout(5.0)
	print ("start streaming")
	while True:
		try:
			msg = local_socket.recv(1024)
			ciphermsg = encrypt(msg, key, iv)
			print (msg)
			client.sendall(msg)
		except:
			break
			
	client.close()
	local_socket.close()
	server.close()
	return 0
	
#def initialConnection():
	#NFC truc	


sendFile('./img.jpg', 'localhost', 3000)	
			
