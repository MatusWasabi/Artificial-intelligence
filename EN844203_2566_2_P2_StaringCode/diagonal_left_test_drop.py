from board import Board

print("Board 3 test diagonal left")
number_of_piece_check = 3
board3 = Board(6, 7)

test_board = [[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, 'O', 'X', None, None, None, None],
['X', 'X', 'X', None, None, None, None]]

board3.EditBoard(test_board)
board3.DropPiece(2, "O")