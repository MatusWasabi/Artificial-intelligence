class Board():
    def __init__(self, col_num, row_num):
        self.col_num = col_num
        self.row_num = row_num
        self.board_space = [[" "] * col_num] * row_num

    def DrawBoard(self) -> None:
        for row in self.board_space:
            print(row)

if __name__ == "__main__":
    board = Board(6, 7)
    board.DrawBoard()