from typing import bool
from ElevatorController import ElevatorController
from elevatorStatus import ElevatorStatus
from request import Request
    

class Floor:
    def __init__(self, floorNum: int ) -> None:
        self.floorNum: int = floorNum
        self.upSelected: bool = False
        self.downSelected: bool =  False

    def selectUp(self, controller) -> None:
        self.upSelected =  True
        controller.floorRequests.put(Request(ElevatorStatus.UP, self.floorNum))
        
    
    def selectDown(self, controller) -> None:
        self.downSelected = True
        controller.floorRequests.put(Request(ElevatorStatus.DOWN, self.floorNum))
    
    def reset(self) -> None:
        pass

    
