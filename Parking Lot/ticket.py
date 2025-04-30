from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from vehicle import Vehicle
from ParkingFloor import ParkingFloor
from ParkingSpot import *
import uuid

@dataclass
class Ticket:
    ticketId: uuid.UUID
    entryTime: datetime
    vehicle: Vehicle
    floor: ParkingFloor
    spot: ParkingSpot
    totalPricing: float
    exitTime: Optional[datetime] = None
    