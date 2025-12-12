import time
from constants import SOLVE_DELAY

class SudokuSolver:
    def __init__(self, board, visualizer=None):
        self.board = board
        self.visualizer = visualizer
        self.steps = 0
        self.backtracks = 0
        self.should_stop = False

    def solve(self, animate=True):
        self.steps = 0
        self.backtracks = 0
        self.should_stop = False
        result = self._dfs(animate)
        if result and self.visualizer:
            self.visualizer.mark_complete()
        return result

    def _dfs(self, animate):
        if self.should_stop:
            return False

        empty = self.board.find_empty()
        if not empty:
            return True

        row, col = empty
        self.steps += 1

        for num in range(1, 10):
            if self.should_stop:
                return False

            if self.board.is_valid_move(row, col, num):
                self.board.set_value(row, col, num)

                if animate and self.visualizer:
                    self.visualizer.draw(
                        current_cell=(row, col),
                        trying_value=num,
                        steps=self.steps,
                        backtracks=self.backtracks
                    )
                    time.sleep(SOLVE_DELAY)

                if self._dfs(animate):
                    return True

                self.board.set_value(row, col, 0)
                self.backtracks += 1

                if animate and self.visualizer:
                    self.visualizer.draw(
                        current_cell=(row, col),
                        backtracking=True,
                        steps=self.steps,
                        backtracks=self.backtracks
                    )
                    time.sleep(SOLVE_DELAY / 2)

        return False

    def get_stats(self):
        return {
            "steps": self.steps,
            "backtracks": self.backtracks
        }
