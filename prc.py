import socket
import settings
from func import *
import time
def main():
	sock = socket.socket()
	
	sock.connect(settings.HOST)
	
	SendToServer(sock, 'PASS {}'.format(settings.pwd))
	SendToServer(sock, 'NICK {}'.format(settings.nick))
	SendToServer(sock, 'JOIN {}'.format(settings.channel))
	
	data = ' '
	
	while True:
		while data:
			i = 2
			if i == 2:
				print('Viewers: {}'.format(getViewersCount()))
				print('Time: {}'.format(getUpdatedTime()))
				i = 0
			else:
				i += 1
			data = sock.recv(1024)
			ReceiveMail(sock, data)
		else:
			continue
		time.sleep(0.5)
if __name__ == '__main__':
	main()