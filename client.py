import socket
import time
import threading
from serverConfig import HOST, PORT
def receive_data(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                msg = data.decode()
                print(msg)

        except BlockingIOError:
            pass
        time.sleep(0.1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("command format: <elevator1/2> [[move <floor>] | disp]")
    receiver_thread = threading.Thread(target=receive_data, args=(s,))
    receiver_thread.daemon = True
    receiver_thread.start()
    while True:
        try:
            data = input()
            s.sendall(data.encode())

        except BlockingIOError:
            pass