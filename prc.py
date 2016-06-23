#!/usr/bin/python
import socket
import settings
from func import *
import time
from PyQt4 import uic, QtGui
import sys

def main():
	app = QtGui.QApplication(sys.argv)
	sock = socket.socket()
	
	sock.connect(settings.HOST)
	
	SendToServer(sock, 'PASS {}'.format(settings.pwd))
	SendToServer(sock, 'NICK {}'.format(settings.nick))
	SendToServer(sock, 'JOIN {}'.format(settings.channel))
	
	data = ' '
	gui = uic.loadUi('123.ui')
	gui.show()
	while data:
		i = 2
		if i == 2:
			gui.ViewerNum.value = getViewersCount()
			print('Time: {}'.format(getUpdatedTime()))
			i = 0
		else:
			i += 1
		data = sock.recv(1024)
		ReceiveMail(sock, data, gui.Chat)
	time.sleep(0.5)
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()