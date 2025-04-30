from collections import Queue
from typing import Dict, Deque
from floors import Floor

class ElevatorContoller:
    _instance = None
    def __new__(cls)  -> None:
        if not cls._instance:
           cls._instance = super(ElevatorContoller, cls).__new__(cls)
        return  cls._instance
    
    def __init__(self, floorNum):
        # Initialize the instance with a value
        if not hasattr(self, 'initialized'):  # Ensure initialization happens only once
            self.floors = [Floor(i) for i in range(floorNum)]
            self.elevators = set()
            self.floorRequests = Queue()
            self.initialized = True
    
    def assignOptimalElevator(self, currFloor, dest) -> None:
        pass

            
    def startElevator(elevatorId, direction: str, dest: int ) -> None:
        pass

    def stopEvelator(elevatorId, elevator) -> None:
        pass

 