import socket
s = socket.socket()
host = 	socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
  c, addr = s.accept()
  print 'got connection from', addr
  c.send('Thank you for connecting')
  print c.recv(1024)
  c.close()