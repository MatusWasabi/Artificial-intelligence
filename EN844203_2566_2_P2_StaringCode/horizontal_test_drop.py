from board import Board

print("Board 2 test horizontal")
number_of_piece_check = 3
board2 = Board(6, 7)
for i in range(number_of_piece_check):
    board2.DropPiece(i, "X")
board2.DropPiece(number_of_piece_check , "O")
board2.DropPiece(number_of_piece_check + 1, "X")