import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pygame
from constants import *
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from sudoku_visualizer import SudokuVisualizer
from puzzles import PUZZLES

class SudokuApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Playable Sudoku")
        self.clock = pygame.time.Clock()
        self.running = True
        self.solving = False
        self.load_puzzle("easy")

    def load_puzzle(self, level):
        self.board = SudokuBoard(PUZZLES[level])
        self.visualizer = SudokuVisualizer(self.screen, self.board)
        self.solver = SudokuSolver(self.board, self.visualizer)
        self.visualizer.draw()

    def run(self):
        while self.running:
            self.handle_events()
            self.visualizer.draw()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.solver.should_stop = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y >= 50:
                    row = (y - 50) // CELL_SIZE
                    col = x // CELL_SIZE
                    if 0 <= row < 9 and 0 <= col < 9:
                        self.visualizer.selected = (row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.solver.should_stop = True

                if event.key == pygame.K_r:
                    self.board.reset()

                if event.key == pygame.K_SPACE and not self.solving:
                    self.solving = True
                    self.solver.solve()
                    self.solving = False

                if self.visualizer.selected:
                    row, col = self.visualizer.selected

                    if self.board.is_fixed(row, col):
                        return

                    if event.key in range(pygame.K_1, pygame.K_9 + 1):
                        num = event.key - pygame.K_0
                        if self.board.is_valid_move(row, col, num):
                            self.board.set_value(row, col, num)

                    if event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                        self.board.set_value(row, col, 0)

if __name__ == "__main__":
    SudokuApp().run()
