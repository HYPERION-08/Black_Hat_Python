import sys
import socket
from datetime import datetime as dt

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # this translates the hostname or ip to ipv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")


print("""
                                                      
 ___  ___ __ _ _ __  _ __   ___ _ __ 
/ __|/ __/ _` | '_ \\| '_ \\ / _ \\ '__|
\\__ \\ (_| (_| | | | | | | |  __/ |   
|___/\\___\\__,_|_| |_|_| |_|\\___|_|   
                                     
                                    
""")

print("Scanning target "+target)
print("Time startd: "+str(dt.now()))
try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # returns with an error indicator with 0 and 1

		if result == 0: # if there are no errors
			print(f"Port {port} is open")

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error:
	print("Could not connect to the server")
	sys.exit()