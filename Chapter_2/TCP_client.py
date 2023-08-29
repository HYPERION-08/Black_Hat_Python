import socket

target_host = "localhost"
target_port = 9997


## AF_INET = address family towards ipv4
## SOCK_STREAM = stream connection 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: Test.com\r\n\r\n")

# recieve some data

response = client.recv(4096)

print(response.decode())
client.close()