import socket 
import threading

ip = "localhost"
port = 9997

def main():
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((ip,port)) # bind() >> "bind" refers to the process of associating a network socket with a specific network address and port 
	server.listen(5) # upto 5 connections
	print(f'[*] Listening on {ip}:{port}')

	while True:
		client,address = server.accept()
		print(f'[*] Accepted connection from {address[0]}:{address[1]}')
		# client >> represents the connection
		# address is containing the ip and port

		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()

		# threading.Thread >> this allows to manage threads for concurrent execution
		# target= >> specifies the function
		# args= >> specifies the parameter to be passed in this case >> client object


def handle_client(client_socket):
	with client_socket as sock: 
		request = sock.recv(1024) # receiving data from the remote connection
		print(f'[*] Received: {request.decode("utf-8")}') # decoding it
		sock.send(b'Acknowledged') # sending a response

if __name__ == '__main__':
	main()