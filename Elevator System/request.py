from dataclasses import dataclass
from elevatorStatus import ElevatorStatus

@dataclass(frozen=True)
class Request:
    direction: ElevatorStatus
    floor: int

    