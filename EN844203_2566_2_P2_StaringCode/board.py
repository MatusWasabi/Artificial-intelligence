class Board():
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.board_space = [[None] * col_num for _ in range(row_num)]

    def DrawBoard(self) -> None:
        for row in self.board_space:
            print(row)
        print()

    def EditBoard(self, new_board: list[list]) -> None:
        self.board_space = new_board
        print("This is new board")
        self.DrawBoard()


    def DropPiece(self, col_num: int, piece_drop: str):
        print(f"Drop {piece_drop} at col {col_num}")
        # Loop from last row to first
        for row in range(len(self.board_space) - 1, -1, -1):

            # Check if that row at col is empty to drop
            if(self.board_space[row][col_num]) == None:
                self.board_space[row][col_num] = piece_drop
        
                self.CheckVertical(piece_drop, col_num)
                self.CheckHorizontal(piece_drop, row)
                self.CheckDiagonalLeft(piece_drop, row, col_num)
                self.CheckDiagonalRight(piece_drop, row, col_num)

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
                break

        print(f"Horizontal piece check {piece_check} get {number_of_piece_check}")
            
        return number_of_piece_check

    def CheckDiagonalLeft(self, piece_check: str, row_num, col_num) -> int:
        number_of_piece_check = 0 
        #Checking it from top to down left

        for index in range(len(self.board_space)):
            try:
                if self.board_space[row_num + index][col_num - index] == piece_check:
                    number_of_piece_check += 1

                elif self.board_space[row_num + index][col_num - index] == None:
                    pass

                else:
                    break

            except IndexError:
                break

        print(f"Diagonal left piece check {piece_check} get {number_of_piece_check}")
            
        return number_of_piece_check
    
    def CheckDiagonalRight(self, piece_check: str, row_num, col_num) -> int:
        number_of_piece_check = 0 
        #Checking it from top to down left

        for index in range(len(self.board_space)):
            try:
                if self.board_space[row_num + index][col_num + index] == piece_check:
                    number_of_piece_check += 1

                elif self.board_space[row_num + index][col_num + index] == None:
                    pass

                else:
                    break

            except IndexError:
                break

        print(f"Diagonal right piece check {piece_check} get {number_of_piece_check}")
            
        return number_of_piece_check
            

    

if __name__ == "__main__":

    # Pass
    #import vertical_test_drop

    #TODO
    #Right now, it is checking just from right and when there is what we are not searching for
    #The number always is 0. Which we do not want that 
    #import horizontal_test_drop

    #Pass
    #import diagonal_left_test_drop

    #Pass
    #import diagonal_right_test_drop

    pass