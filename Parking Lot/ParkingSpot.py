from dataclasses import dataclass
from vehicle import VehicleType

@dataclass
class ParkingSpot:
    type: VehicleType


k = ParkingSpot(VehicleType.BIKE)
print(k)