import sys
import socket
import getopt
import threading
import subprocess

listen = False
upload = False
command = False
execute = ""
target = ""
upload_destination = ""
port = 0

def run_command(cmd):
	cmd = cmd.rstrip() #num:1
	try:
		output = subprocess.check_output(cmd, stderr=subprocess.STDOUT,shell=True) #num:2
	except subprocess.CalledProcessError as e: #num:3
		output = e.output
	return output

	

if __name__ == '__main__':
	main()