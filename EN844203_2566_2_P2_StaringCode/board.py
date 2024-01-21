class Board():
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.board_space = [[None] * col_num for _ in range(row_num)]

    def DrawBoard(self) -> None:
        for row in self.board_space:
            print(row)

        print()

    def DropPiece(self, col_num: int, piece_drop: str):

        print(f"Drop {piece_drop} at col {col_num}")
        # Loop from last row to first
        for row in range(len(self.board_space) - 1, -1, -1):

            # Check if that row at col is empty to drop
            if(self.board_space[row][col_num]) == None:
                self.board_space[row][col_num] = piece_drop
        
                #self.CheckVertical(piece_drop, col_num)
                self.CheckHorizontal(piece_drop, row)
                return self.DrawBoard()      
            
        # Check Connect


    def CheckVertical(self, piece_check: str, col_num):
        number_of_piece_check = 0
        #Check it from top to bottom
        for row in self.board_space:
            if row[col_num] == piece_check:
                number_of_piece_check += 1

            elif row[col_num] == None:
                pass

            else:
                print(f"Found {row[col_num]} instead of {piece_check}")
                print("Stop checking")
                break
            

        print(f"Vertical piece check {piece_check} get {number_of_piece_check}")
        return number_of_piece_check
        pass

    def CheckHorizontal(self, piece_check: str, row_num) -> int:
        number_of_piece_check = 0 
        #Checking it from right to left
        for item in reversed(self.board_space[row_num]):
            if item == piece_check:
                number_of_piece_check += 1

            elif item == None:
                pass

            else:
                print(f"Found {item} instad of {piece_check}")
                print("Stop checking")
                break

        print(f"Horizontal piece check {piece_check} get {number_of_piece_check}")
            
        return number_of_piece_check
        pass

    def CheckDiagonal() -> bool:
        pass
            

    

if __name__ == "__main__":
    board = Board(6, 7)
    board.DrawBoard()


"""    # Vertical Test Passed
    for i in range(3):
        board.DropPiece(0 ,"X")

    board.DropPiece(0, "O")

    board.DropPiece(0, "X")"""

# Horizontal Test 1 PAssed
number_of_piece_check = 3
for i in range(number_of_piece_check):
    board.DropPiece(i, "X")

#Horizontal Test 2 Passed
board.DropPiece(number_of_piece_check , "O")
board.DropPiece(number_of_piece_check + 1, "X")