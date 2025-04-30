from vehicle import Vehicle, VehicleType
from pricingStrategy import *
from ParkingFloor import ParkingFloor
from ticket import Ticket
from collections import deque
from dataclasses import dataclass
from typing import Optional, Deque, Tuple
from datetime import datetime
import uuid

class ParkingLot:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance.floors = [] 
            cls._instance.availableSlots =  deque()
            cls._instance.pricingStrategy = None
        return cls._instance
        
        
    def setPricingStrategy(self, strategy: PricingStrategy):
        self.pricingStrategy = strategy


    def addFloor(self, floor: ParkingFloor) -> None:
        self.floors.append(floor)
    
    def availableSlots(self) -> None:
        for ind, floor in enumerate(self.floors):
            print(f'Displaying slots for Floor{ind}')
            for spot in floor.availableSpots:
                print(spot)
    

    def reserveSpot(self) -> Tuple:
        for ind, floor in enumerate(self.floors):
            if floor.availableSpots:
                spot = floor.availableSpots.popleft()
                floor = ind
                return floor, spot

    def parkVehicle(self, vehicle: Vehicle) -> Ticket:
        floor, spot = self.reserveSpot()
        ticket = Ticket(
            ticketId=uuid.uuid4(), entrytime=datetime.now(),
            vehicle= vehicle, spot = spot, floor = floor
        )
        return ticket


    def unparkVehicle(self, ticket: Ticket) -> Ticket:
        ticket.exitTime = datetime.now()
        self.floors[ticket.floor].availableSpots.addSpot(ticket.spot)
        ticket.totalPricing = self.pricingStrategy.calculateCharges(ticket)
        return Ticket
        
    
    
park = ParkingLot()
flatRate = FlatRatePricing(5)
print(park, flatRate)
park.setPricingStrategy(flatRate)
print(park.pricingStrategy.flatRate)
        













            


    
        

    




