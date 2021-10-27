import pyautogui as pyautogui
import pygame, sys
from gui import Gui
from board import Board
from AI import AI

pygame.init()
gui = Gui()
AI_ranking = AI()
pisk_board = Board()
screen = pygame.display.set_mode((gui.WIDTH, gui.HEIGHT))
pygame.display.set_caption('Piškvorky')
screen.fill(gui.BG_COLOR)
gui.draw_lines(screen)
player = 1
game_over = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // gui.SQUARE_SIZE)
            clicked_col = int(mouseX // gui.SQUARE_SIZE)

            if pisk_board.available_square(clicked_row, clicked_col):
                pisk_board.mark_square(clicked_row, clicked_col, 1)

                pisk_board.game_board = AI_ranking.ai_ranking(pisk_board.game_board,2)
                winner = pisk_board.evaluate()
                if winner != 0:
                    game_over = True

        gui.draw_figures(pisk_board.game_board, screen)

    gui.draw_figures(pisk_board.game_board, screen)
    pygame.display.update()
    winner = pisk_board.evaluate()
    if winner != 0:
        pyautogui.alert("Winner is player: " + str(winner))
        sys.exit()