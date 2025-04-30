from enum import Enum
from abc import ABC, abstractmethod
from typing import Tuple


class PieceColor(str, Enum):
    WHITE = 'White'
    BLACK = 'Black'

class PieceType(Enum):
    KING = 1
    QUEEN = 2
    BISHOP= 3
    KNIGHT = 4
    ROOK = 5
    PAWN = 6


class Piece(ABC):
    def __init__(self, color, positon):
        self.color = color
        self.position = positon


    @abstractmethod
    def validMove(self, board, start, end):
        pass

    @abstractmethod
    def move(self, board, start, end):
        pass


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        

    def validMove(self, board, start, end):
        pass

    def move(self, board, start, end):
        pass

    def __repr__(self):
        return  self.color + " " + __class__.__name__ 


class King(Piece):
    def __init__(self, color):
        self.color = color

    def validMove(self, board, start, end):
        pass

    def move(self, board, start, end):
        pass


class Queen(Piece):
    def __init__(self, color):
        self.color = color

    def validMove(self, board, start, end):
        pass

    def move(self, board, start, end):
        pass



class PieceFactory:
        @staticmethod
        def createPiece(type: PieceType, color: PieceColor, positon: Tuple) -> Piece:
            pieceMap = {
                PieceType.KING: King,
                PieceType.QUEEN: Queen,
                PieceType.ROOK: Rook
            }

            piece = pieceMap.get(type)
            return piece(color, positon)
             

print(PieceFactory.createPiece(PieceType.ROOK, PieceColor.BLACK, (0, 0)))
    