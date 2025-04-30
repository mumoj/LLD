from elevatorStatus import ElevatorStatus
class Elevator:
    def __init__(self, elevatorId, capacity):
        self.capacity = capacity
        self.status = ElevatorStatus.IDLE
        self.requests = set()
        self.currentFloor = 0


    def move(self):
        if self.status == ElevatorStatus.UP:
            self.currentFloor += 1
            
        elif self.status == Elevator.DOWN:
            self.currentFloor -= 1

    def moveToFloor(self, floor, maxFloor):
        pass
        



