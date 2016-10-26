import socket
import commands

host = "192.168.3.5"
port = 41300

known_sig = "c974b779d095f5772a36e2139276ffdc"
known_text = "testing connection"

def test(sign, text):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  sock.connect((host, port))
  
  data = sign + " " + text
  sock.send(data)
  return sock.recv(4096)

for i in range(1,32):
  cmd = "/usr/local/Cellar/hashpump/1.2.0/bin/hashpump"
  cmd += " -s " + known_sig
  cmd += " -d \"" + known_text + "\""
  cmd += " -k " + str(i)
  cmd += " -a " + "AAAA"
  sign, text = commands.getoutput(cmd).split('\n')
  a, b = text.split('\\x80')
  b = b[:-4].replace('\\x','').decode('hex')

  data = a + '\x80' + b + 'AAAA'
  res = test(sign, data)
  print str(i) + ': ' + res
  if not 'Wrong' in res:
    break