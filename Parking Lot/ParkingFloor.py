from dataclasses import dataclass, field
from ParkingSpot import *
from  collections import deque
from typing import Deque

@dataclass
class ParkingFloor:
    availableSpots: Deque[ParkingSpot] = field(default_factory=deque)

    def addSpot(self, spot: ParkingSpot):
        self.availableSpots.append(spot)


p = ParkingFloor(availableSpots= deque())
print(p)