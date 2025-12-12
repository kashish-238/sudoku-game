class SudokuBoard:
    def __init__(self, puzzle):
        self.original = [row[:] for row in puzzle]
        self.board = [row[:] for row in puzzle]
        self.size = 9

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return r, c
        return None

    def is_valid_move(self, row, col, num):
        if num in self.board[row]:
            return False

        for r in range(9):
            if self.board[r][col] == num:
                return False

        box_r, box_c = (row // 3) * 3, (col // 3) * 3
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if self.board[r][c] == num:
                    return False

        return True

    def set_value(self, row, col, value):
        self.board[row][col] = value

    def get_value(self, row, col):
        return self.board[row][col]

    def is_fixed(self, row, col):
        return self.original[row][col] != 0

    def reset(self):
        self.board = [row[:] for row in self.original]
