from board import Board

print("Board 1 test vertical")
board = Board(6, 7)
board.DrawBoard()
for i in range(3):
    board.DropPiece(0 ,"X")
board.DropPiece(0, "O")
board.DropPiece(0, "X")