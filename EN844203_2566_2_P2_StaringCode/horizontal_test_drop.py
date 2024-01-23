from board import Board

print("Board 2 test horizontal")
number_of_piece_check = 3
board2 = Board(6, 7)

# This is simple checking for horizontal
case1 = [[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
['X', 'X', None, None, None, None, None]]
board2.EditBoard(case1)
board2.DropPiece(2, "X")

#When there is something unwanted found scanning from right to left
case2 = [[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
['X', 'X', "O", None, None, None, None]]
board2.EditBoard(case2)
board2.DropPiece(3, "X")


#When checking for something in between 
case3 = [[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, "X", "O", None, None, None]]
board2.EditBoard(case3)
board2.DropPiece(1, "X")