import time

class Elevator:
    def __init__(self,
                    maxFloor: int       = 10,
                    movementSpeed: int  = 1,
                    elevatorTag: int    = 0,
                    debugMsg: bool      = True,
                    ) -> None:
        
        self.currentFloor: int  = 0
        self.maxFloor           = maxFloor
        self.movementSpeed      = movementSpeed    
        self.elevatorTag        = elevatorTag       # user shuld specify elevator tag
        self.debugMsg           = debugMsg
    def display_floor(self) -> str:
        message =   f"--------- Elevator {self.elevatorTag} ------------------\n" + \
                    f"--------- currently at {self.currentFloor} Floor --------\n" + \
                    f"---------------------------------------"
        if self.debugMsg:
            print(message)
            
        return message
        
    def move(self, conn, floor: int) -> None:
        
        if floor < 0 or floor > 10:
            if conn:
                conn.sendall(b"currentFloor needs to be within the range of 0 ~ 10")
            return 
        
        if self.currentFloor == floor:
            if conn:
                conn.sendall(self.display_floor().encode())
            return
        
        step: int = 0
        if self.currentFloor < floor:
            step = 1
        elif self.currentFloor > floor:
            step = -1
            
        for _ in range(self.currentFloor, floor, step):
            self.currentFloor += step
            if conn:
                conn.sendall(self.display_floor().encode())
            time.sleep(self.movementSpeed)
            
