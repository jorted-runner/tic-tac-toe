from board_info import playable_positions, board
from brain import check_win, play_piece
import random

player = 1
playing = True
turns = 0

while playing:
    print(f"\nPlayer {player}")
    input_needed = True
    while input_needed:
        try:
            column = int(input("Enter which column you want to play in: (1-3) "))
            row = int(input("Enter which row you want to play in: (1-3) "))
            input_needed = False
        except ValueError:
            print("Must be a number between 1-3, try again.\n")

    played_pos = (column, row)

    if played_pos in playable_positions:
        played = playable_positions.pop(played_pos)
        player = play_piece(player, column, row, played)
                  
        for i in range(0,3):
            print(f"{board[i][0]}|{board[i][1]}|{board[i][2]}")
            if i == 0 or i == 1:
                print("------------")
        winner, who_won = check_win()
        if winner:
            print(f"Congrats {who_won} wins!")
            playing = False
        turns += 1
        if turns == 9 and not winner:
            print("No one won! You both lose.")
            playing = False
    else:
        print("Not so fast, you can't play there!")