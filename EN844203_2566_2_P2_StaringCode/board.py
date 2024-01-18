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
        
                self.CheckVertical(piece_drop, col_num)
                return self.DrawBoard()      
            
        # Check Connect


    def CheckVertical(self, piece_check: str, col_num):
        number_of_piece_check = 0
        for row in self.board_space:
            if row[col_num] == piece_check:
                number_of_piece_check += 1

            elif row[col_num] == None:
                pass

            else:
                print(f"Found {row[col_num]} instead of {piece_check} Stop checking")
                print(f"Piece check {piece_check} get {number_of_piece_check}")
                return number_of_piece_check

        print(f"Piece check {piece_check} get {number_of_piece_check}")
            
        return number_of_piece_check

        # Know where it is dropped
        # Check if position [row - 1][col], [row - 2][col] until the piece is not what we want to check
        # Return out the number that we can fund 



        pass

    def CheckHorizontal() -> bool:
        pass

    def CheckDiagonal() -> bool:
        pass
            

    

if __name__ == "__main__":
    board = Board(6, 7)
    board.DrawBoard()

    for i in range(3):
        board.DropPiece(0 ,"X")

    board.DropPiece(0, "O")

    board.DropPiece(0, "X")
