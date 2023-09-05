import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading


def execute(cmd):
	cmd = cmd.strip()
	if not cmd:
		return 
	output = subprocess.check_ouput(shlex.split(cmd),stderr=subprocess.STDOUT)
	return output.decode()