from pieces import PieceFactory, PieceType, PieceColor

class Board:
    def __init__(self, rows, cols):
        self.board = [ [None for i in range(cols)] for i in range(rows) ]
        self.initialize()


    def initiliaze(self) -> "Board":
        return self
    
    def display(self) -> None:
        pass

   

    
        

    