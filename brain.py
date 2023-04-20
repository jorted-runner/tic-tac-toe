from board_info import board, p1_placements, p2_placements, winning_combos

def check_win():
    p1 = sorted(p1_placements)
    p2 = sorted(p2_placements)
    for row in winning_combos:
        check_p1 = [i for i, j in zip(row, p1) if i == j]
        check_p2 = [i for i, j in zip(row, p2) if i == j]
        if check_p1 == row:
            return True, "Player 1"
        elif check_p2 == row:
            return True, "Player 2"
    return False, ""

def play_piece(player, x, y, position):
    if player == 1:
        board[y-1][x-1] = " X "
        p1_placements.append(position)
        player = 2
    else:
        board[y-1][x-1] = " O "
        p2_placements.append(position)
        player = 1
    return player