import numpy as np


class Board:

    def __init__(self):
        self.game_board = (np.zeros((30, 30)))

    def row_win(self, player):
        win = False
        for x in range(len(self.game_board)):
            count = 0
            for y in range(len(self.game_board)):
                if self.game_board[x, y] == player:
                    count = count + 1
                    if count > 4:
                        self.game_board[x, y] = player
                        print(self.game_board)
                        win = True

                if self.game_board[x, y] != player:
                    count = 0
                    continue

            if win:
                return win
        return win

    def col_win(self, player):
        win = False
        for y in range(len(self.game_board)):
            count = 0
            for x in range(len(self.game_board)):

                if self.game_board[x, y] == player:
                    count = count + 1
                    if count > 4:
                        self.game_board[x, y] = player
                        print(self.game_board)
                        win = True

                if self.game_board[x, y] != player:
                    count = 0

            if win:
                return win
        return win

    def diag_win(self, player):
        ln = 1
        win = False
        for x in range(len(self.game_board)):
            count = 0
            const = 0
            ln += 1
            for y in range(ln - 1):

                if self.game_board[const, x - const] == player:
                    count = count + 1

                    if count > 4:
                        self.game_board[const, x - const] = player
                        print(self.game_board)
                        win = True

                if self.game_board[const, x - const] != player:
                    count = 0

                const += 1

        self.game_board = np.rot90(self.game_board, k=1, axes=(1, 0))
        ln = 1
        for x in range(len(self.game_board)):
            count = 0
            const = 0
            ln += 1
            for y in range(ln - 1):

                if self.game_board[const, x - const] == player:
                    count = count + 1

                    if count > 4:
                        self.game_board[const, x - const] = player
                        print(self.game_board)
                        win = True

                if self.game_board[const, x - const] != player:
                    count = 0

                const += 1

        self.game_board = np.rot90(self.game_board, k=1, axes=(1, 0))
        ln = 1
        for x in range(len(self.game_board)):
            count = 0
            const = 0
            ln += 1
            for y in range(ln - 1):

                if self.game_board[const, x - const] == player:
                    count = count + 1

                    if count > 4:
                        self.game_board[const, x - const] = player
                        print(self.game_board)
                        win = True

                if self.game_board[const, x - const] != player:
                    count = 0

                const += 1

        self.game_board = np.rot90(self.game_board, k=1, axes=(1, 0))
        ln = 1
        for x in range(len(self.game_board)):
            count = 0
            const = 0
            ln += 1
            for y in range(ln - 1):

                if self.game_board[const, x - const] == player:
                    count = count + 1

                    if count > 4:
                        self.game_board[const, x - const] = player
                        win = True

                if self.game_board[const, x - const] != player:
                    count = 0

                const += 1

        self.game_board = np.rot90(self.game_board, k=1, axes=(1, 0))

        return win

    def evaluate(self):
        winner = 0

        for player in [1, 2]:
            if (self.row_win(player) or
                    self.col_win(player) or
                    self.diag_win(player)):
                winner = player

        if np.all(self.game_board != 0) and winner == 0:
            winner = -1
        return winner

    def mark_square(self, row, col, player):
        self.game_board[row][col] = player

    def available_square(self, row, col):
        return self.game_board[row][col] == 0
