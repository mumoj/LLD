selectFLoor -> determineDirection ->  if UP:
   Floor                                 - check all elevetors level or below going up: Scan list downwards greedily?
                                    - pick  the nearest one also going up, if not the furthest one going in the opposite direction.

                                        |
                                Once Elevator Picked; if up, sort floors in asc order
                                                      if down, sort floors in desc order
                                          
                                        |

                                stop elevator at each position, popping  a floor at each stop

                                        |

                                Once an elevetor reaches top, it reverses direction; same with the ground floor
                                       
                                        

up: []
down: []
Inactive: []

ElevatorSystem:
   controller.run()


ElevatorController:
   + elevators: Set
   + requests: Queue
   + floors
   
   - assignOptimalElevator(elevatarMap)
   - _calculateElevatorCost()
   - run()
   - stopEvelator(floor)
   - startElevator()


ElevatorStatus:
   IDLE: 1
   UP: 2
   DOWN: 3
   MAINTENANCE: 4
   EMERGENCY: 5

Elevator:
   + capacity: float
   + status: Enum
   + currentFloor: Floor
   + destRequests: Set
   + door: Door

   - move()
   - moveToFloor()
   - onboardUser(User)
   - checkCapacity()


DoorStatus:
   OPEN: 1
   CLOSED: 2

Door:
status: DoorStatus

Floor:
   + upSelected: bool
   + downSelected: bool

   -selectUpButton() 
   -selectDownButton()
   -sendRequest()
   -reset()








    

    
    



                                     

    A  I
[0, 1, 2, 3, 4, 5]
 B              C  