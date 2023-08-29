import socket

target_host = "localhost"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
client.sendto(b'this is the data',(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()


### usege-----
# nc -ulp 80
## as this is a udp client