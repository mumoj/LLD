Populate board -> First Player Moves Piece -> Play Switches to the Second Player -> Second Player moves Piece ....until Check Mate

                                                                       Piece
                                                                    -color                                                +validMove(start, end, board)
                                                                     +move

                                                                        |

                                                    Rook(Piece):
                                                       - color

                                                       + validMove(start, end, board)              
                                                       + move(start, end, board)

Board
- noOfRows                                          PieceFactory():
                                                        - PieceMap                                                       + createPiece(color,                                               
- noofCols
+ createBoard()
+ arrangePieces()



ChessGame
- board: Board
- players: Queue(size=2)

+ startGame()
+ makeMove(start, end)
+ switchPlay()
+ checkStatus()


Pieces
Rook
Pawn
Bishop
King
Queen
Knight
                                                                                                  
