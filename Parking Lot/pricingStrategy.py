from abc import ABC, abstractmethod
from typing import Dict
from datetime import datetime

# Base class for pricing strategies
class PricingStrategy(ABC):
    
    @abstractmethod
    def calculate_cost(self, vehicle_type: str, duration: float) -> float:
        raise NotImplementedError

# Vehicle-specific pricing
class VehicleTypePricing(PricingStrategy):
    def __init__(self, rates: Dict[str, float]):
        self.rates = rates  # Rates per hour for each vehicle type

    def calculate_cost(self, ticket) -> float:
        if ticket.vehicle.vehicleType not in self.rates:
            raise ValueError(f"No rate defined for vehicle type: {ticket.vehicleType}.")
        return self.rates[ticket.vehicle.vehicleType] * ticket.duration
    

class FlatRatePricing(PricingStrategy):
    def __init__(self, flat_rate):
        self.flatRate = flat_rate  # Rates per hour for each vehicle type

    def calculate_cost(self, ticket) -> float:
        return self.flatRate * ticket.duration
    

class PeakHourPricing(PricingStrategy):
    def __init__(self, peakHour, startTime, endTime, multiplier, flatRate):
        self.peakHour = peakHour
        self.startTime = startTime
        self.endTime = self.endTime
        self.flatRate = flatRate
        self.multiplier = multiplier

    def calculate_cost(self, ticket) -> float:
        if datetime.now() >= self.startTime and datetime.now < self.endTime:
            return self.multiplier * ticket.duration * self.flatRate
        return self.flatRate * ticket.duration

    
flat = FlatRatePricing(5)
print(flat)