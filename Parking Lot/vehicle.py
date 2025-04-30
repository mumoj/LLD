from dataclasses import dataclass
from enum import Enum

class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    TRUCK = "Truck"

@dataclass
class Vehicle:
    licensePlate : str
    vehicleType: VehicleType


v = Vehicle('800', VehicleType.TRUCK)
print(v)





