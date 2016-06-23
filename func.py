import json
from datetime import *
import helpclass
import settings
import pycurl
file1 = open('MatList.txt', 'r')
MatList = helpclass.help.loadListFromFile(file1)
def SendToServer(sock, msg):
  sock.send('{}\n'.format(msg))
def ReceiveMail(sock, msg):
  msg = msg.split('\n')
  for i in msg:
    i = i.split(' ', 3)
    if i[0] == '':
      continue
    elif i[0] == 'PING':
      SendToServer(sock, 'PONG {}'.format(i[1]))
    elif i[1] == 'PRIVMSG':
      aut = i[0].split('!')[0]
      print('>{}: {}'.format(aut[1:], i[3][1:]))
      CatchMat(i[3][1:])
    else:
      print(' '.join(i))
def getURL():
	try:
		import StringIO
	except ImportError:
		from io import StringIO
	c = pycurl.Curl()
	buf = StringIO.StringIO()
	c.setopt(c.URL, 'https://api.twitch.tv/kraken/streams/{}/'.format(settings.channel.split('#')[1]))
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	ret = buf.getvalue()
	buf.close()
	return ret
def getViewersCount():
	import json
	dic = getURL()
	return json.loads(dic)['stream']['viewers']
def getUpdatedTime():
	dic = getURL()
	time = json.loads(dic)['stream']['created_at']
	now = datetime.now()
	time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
	return now - time
def CatchMat(msg):
	pass