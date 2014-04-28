import socket
s = socket.socket()
host = 	socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
  c, addr = a.accept()
  print 'got connection from', addr
  c.send('Thank you for connecting')
  c.close()