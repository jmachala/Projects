import pygame


class Gui:

    def __init__(self):
        self.WIDTH = 750
        self.HEIGHT = 750
        self.LINE_WIDTH = 3
        self.WIN_LINE_WIDTH = 15
        self.BOARD_ROWS = 30
        self.BOARD_COLS = 30
        self.SQUARE_SIZE = 25
        self.CIRCLE_RADIUS = 10
        self.CIRCLE_WIDTH = 3
        self.CROSS_WIDTH = 3
        self.SPACE = 22
        self.RED = (255, 0, 0)
        self.BG_COLOR = (28, 170, 156)
        self.LINE_COLOR = (23, 145, 135)
        self.CIRCLE_COLOR = (239, 231, 200)
        self.CROSS_COLOR = (66, 66, 66)

    def draw_lines(self, screen):
        for i in range(29):
            pygame.draw.line(screen, self.LINE_COLOR, (0, (i + 1) * self.SQUARE_SIZE),
                             (self.WIDTH, (i + 1) * self.SQUARE_SIZE), self.LINE_WIDTH)
            pygame.draw.line(screen, self.LINE_COLOR, ((i + 1) * self.SQUARE_SIZE, 0),
                             ((i + 1) * self.SQUARE_SIZE, self.HEIGHT),
                             self.LINE_WIDTH)

    def draw_figures(self, board, screen):
        for row in range(self.BOARD_ROWS):
            for col in range(self.BOARD_COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, self.CIRCLE_COLOR, (int(col * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                                                                   int(row * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)),
                                       self.CIRCLE_RADIUS,
                                       self.CIRCLE_WIDTH)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, self.CROSS_COLOR,
                                     (col * self.SQUARE_SIZE + self.SPACE,
                                      row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE),
                                     (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                                      row * self.SQUARE_SIZE + self.SPACE), self.CROSS_WIDTH)
                    pygame.draw.line(screen, self.CROSS_COLOR,
                                     (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SPACE),
                                     (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE,
                                      row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE),
                                     self.CROSS_WIDTH)
