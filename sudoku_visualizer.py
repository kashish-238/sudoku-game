import pygame
from constants import *

class SudokuVisualizer:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.small_font = pygame.font.Font(None, SMALL_FONT_SIZE)
        self.selected = None

    def draw(self, current_cell=None, trying_value=None, backtracking=False, steps=0, backtracks=0):
        self.screen.fill(WHITE)
        self._draw_grid()
        self._draw_numbers()
        self._draw_selection()
        pygame.display.flip()

    def _draw_grid(self):
        for i in range(GRID_SIZE + 1):
            thickness = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, BLACK,
                (0, 50 + i * CELL_SIZE),
                (WIDTH, 50 + i * CELL_SIZE),
                thickness
            )
            pygame.draw.line(self.screen, BLACK,
                (i * CELL_SIZE, 50),
                (i * CELL_SIZE, 50 + GRID_SIZE * CELL_SIZE),
                thickness
            )

    def _draw_numbers(self):
        for r in range(9):
            for c in range(9):
                val = self.board.get_value(r, c)
                if val == 0:
                    continue

                color = FIXED_COLOR if self.board.is_fixed(r, c) else BLACK
                x = c * CELL_SIZE + CELL_SIZE // 2
                y = 50 + r * CELL_SIZE + CELL_SIZE // 2
                text = self.font.render(str(val), True, color)
                self.screen.blit(text, text.get_rect(center=(x, y)))

    def _draw_selection(self):
        if self.selected:
            r, c = self.selected
            rect = pygame.Rect(
                c * CELL_SIZE,
                50 + r * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(self.screen, (200, 220, 255), rect, 3)
