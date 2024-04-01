import socket
from scripts.elevator import Elevator
from serverConfig import HOST, PORT

Elevator1 = Elevator(elevatorTag=1)
Elevator2 = Elevator(elevatorTag=2)

def parse(command: str, conn) -> bool:
    command = command.split(" ")
    if not conn:
        return False
    if len(command) < 2:
        return False
    try:
        if command[0] == "elevator1":
            if command[1] == "move":
                Elevator1.move(conn, floor=int(command[2]))
                return True
            elif command[1] == "disp":
                conn.sendall(Elevator1.display_floor().encode())
                return True
            else:
                return False
            
        elif command[0] ==  "elevator2":
            if command[1] == "move":
                Elevator2.move(conn, floor=int(command[2]))
                return True
            elif command[1] == "disp":
                conn.sendall(Elevator2.display_floor().encode())
                return True
        else:
            return False
    except Exception:
        return False
    
    return True

def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    conn.sendall(b"wrong command")
                data = data.decode()
                parseResult = parse(data, conn)
                
                if parseResult == False:
                    conn.sendall(b"command format: <elevator1/2> [[move <floor>] | disp]")    
                
                
if __name__ == "__main__":
    startServer()