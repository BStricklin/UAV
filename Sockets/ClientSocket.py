import socket
import sys
import json

HOST, PORT = "192.168.0.1", 9996
#data = " ".join(sys.argv[1:])
data = ""
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall("sup\n")

    # Receive data from the server and shut down
    data = sock.recv(1024).strip()
    jsData = {}
    jsData = json.loads(data)

finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(jsData)
