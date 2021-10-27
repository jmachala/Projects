class AI:

    def ai_ranking(self, board, player):
        ranking = []
        enemy = 2
        if player == 2:
            enemy = 1

        for x in range(len(board)):
            for y in range(len(board)):
                deff = 1
                att = 1

                rank_updown = 0
                rank_leftright = 0
                rank_diagleft = 0
                rank_diagright = 0

                rank_att_updown = 0
                rank_att_leftright = 0
                rank_att_diagleft = 0
                rank_att_diagright = 0

                const_up = 0
                const_down = 0
                check_up = 1
                check_down = 1

                const_left = 0
                const_right = 0
                check_left = 1
                check_right = 1

                const_diagleftup = 0
                const_diagleftdown = 0
                check_diagleftup = 1
                check_diagleftdown = 1

                const_diagrightup = 0
                const_diagrightdown = 0
                check_diagrightup = 1
                check_diagrightdown = 1

                try:

                    if board[x, y] != 1 and board[x, y] != 2:

                        # směr up/down

                        while check_up == 1:
                            check_up = 0
                            if board[x - 1 - const_up, y] == enemy and deff == 1:
                                rank_updown += 1
                                check_up = 1
                                att = 0
                            if board[x - 1 - const_up, y] == player and att == 1:
                                deff = 0
                                rank_att_updown += 1
                                check_up = 1
                            const_up += 1

                        deff = 1
                        att = 1

                        while check_down == 1:
                            check_down = 0
                            if board[x + 1 + const_down, y] == enemy and deff == 1:
                                rank_updown += 1
                                check_down = 1
                                att = 0
                            if board[x + 1 + const_down, y] == player and att == 1:
                                deff = 0
                                rank_att_updown += 1
                                check_down = 1
                            const_down += 1

                        # směr left/right

                        deff = 1
                        att = 1

                        while check_left == 1:
                            check_left = 0
                            if board[x, y - 1 - const_left] == enemy and deff == 1:
                                rank_leftright += 1
                                check_left = 1
                                att = 0
                            if board[x, y - 1 - const_left] == player and att == 1:
                                deff = 0
                                rank_att_leftright += 1
                                check_left = 1
                            const_left += 1

                        deff = 1
                        att = 1

                        while check_right == 1:
                            check_right = 0
                            if board[x, y + 1 + const_right] == enemy and deff == 1:
                                rank_leftright += 1
                                check_right = 1
                                att = 0
                            if board[x, y + 1 + const_right] == player and att == 1:
                                deff = 0
                                rank_att_leftright += 1
                                check_right = 1
                            const_right += 1

                        # směr \

                        deff = 1
                        att = 1

                        while check_diagleftup == 1:
                            check_diagleftup = 0
                            if board[x - 1 - const_diagleftup, y - 1 - const_diagleftup] == enemy and deff == 1:
                                rank_diagleft += 1
                                check_diagleftup = 1
                                att = 0
                            if board[x - 1 - const_diagleftup, y - 1 - const_diagleftup] == player and att == 1:
                                deff = 0
                                rank_att_diagleft += 1
                                check_diagleftup = 1
                            const_diagleftup += 1

                        deff = 1
                        att = 1

                        while check_diagleftdown == 1:
                            check_diagleftdown = 0
                            if board[x + 1 + const_diagleftdown, y + 1 + const_diagleftdown] == enemy and deff == 1:
                                rank_diagleft += 1
                                check_diagleftdown = 1
                                att = 0
                            if board[x + 1 + const_diagleftdown, y + 1 + const_diagleftdown] == player and att == 1:
                                deff = 0
                                rank_att_diagleft += 1
                                check_diagleftdown = 1
                            const_diagleftdown += 1

                        # směr /

                        deff = 1
                        att = 1

                        while check_diagrightup == 1:
                            check_diagrightup = 0
                            if board[x - 1 - const_diagrightup, y + 1 + const_diagrightup] == enemy and deff == 1:
                                rank_diagright += 1
                                check_diagrightup = 1
                                att = 0
                            if board[x - 1 - const_diagrightup, y + 1 + const_diagrightup] == player and att == 1:
                                deff = 0
                                rank_att_diagright += 1
                                check_diagrightup = 1
                            const_diagrightup += 1

                        deff = 1
                        att = 1

                        while check_diagrightdown == 1:
                            check_diagrightdown = 0
                            if board[x + 1 + const_diagrightdown, y - 1 - const_diagrightdown] == enemy and deff == 1:
                                rank_diagright += 1
                                check_diagrightdown = 1
                                att = 0
                            if board[x + 1 + const_diagrightdown, y - 1 - const_diagrightdown] == player and att == 1:
                                deff = 0
                                rank_att_diagright += 1
                                check_diagrightdown = 1
                            const_diagrightdown += 1

                        rank = 10 ** rank_updown + 10 ** rank_diagleft + 10 ** rank_diagright + 10 ** rank_leftright
                        rank_att = 10 ** rank_att_updown + 10 ** rank_att_diagleft + 10 ** rank_att_diagright + 10 ** rank_att_leftright + 1

                        if rank_att_updown > 3 or rank_att_diagleft > 3 or rank_att_diagright > 3 or rank_att_leftright > 3:
                            rank_att = 10 ** 6
                        ranking.append((x, y, rank, rank_att))

                except:
                    None

        highest_att_rank = 0
        highest_deff_rank = 0
        x_att = 0
        y_att = 0
        x_deff = 0
        y_deff = 0

        for i in range(len(ranking)):

            array = ranking[i]

            if array[2] > highest_deff_rank:
                highest_deff_rank = array[2]
                x_deff = array[0]
                y_deff = array[1]

            if array[3] > highest_att_rank:
                highest_att_rank = array[3]
                x_att = array[0]
                y_att = array[1]

        if highest_att_rank > highest_deff_rank:
            board[x_att, y_att] = player
        else:
            board[x_deff, y_deff] = player

        return (board)
