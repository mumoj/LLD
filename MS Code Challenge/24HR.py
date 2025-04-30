from typing import List

def generateValues(time: str) -> List:
    pos = time.indexof('?')

    if pos == 0:
        return [str(val) for val in range(3)]
    
    if pos == 1 or pos == 4:
        if time[0] == '0' or time[0] == '1' or pos == 4:
            return [str[val] for val in range(10)]
        else:
            return [str[val] for val in range(1, 5)]
        
    if pos == 2:
        return [str[val] for val in range(6)]




