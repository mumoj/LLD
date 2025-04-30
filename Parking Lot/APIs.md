
GET  park/availabilty?page=1&limit=10
     - List of Available Spots
    POST levels/{levelID}
        POST spots/{spotData}

POST  park/{Vehicle} 
    - processes Parking
POST unpark/{VehiclePlate}
    - process Unparking


GET  tickets/{VehiclePlate}
    - Availes ticket data for printing
POST paymnents/{ticketID}
    - Processes Payment


EntryGate  -> parkVehicle       ->     unParkVehicle ->    generateTicket ->            ExitGate
             - Find Floor                 - releaseSpot       - register ExitTime
             - find ParkingSpot                               - calc TicketPrice
             - reserveSpot
             - register ArrivalTime in ticket


Vehicle
ParkingLot                 Ticket
ParkingFloor
Parking Spot
