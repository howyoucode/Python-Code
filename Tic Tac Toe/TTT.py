def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_win(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
]
    return [player, player, player] in win_conditions


def check_tie(board):
    return " " not in board


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    game_on = True

    display_board(board)

    while game_on:
        try:
            move = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1

            if board[move] != " ":
                print("This position is already occupied. Try again.")
                continue

            board[move] = current_player
            display_board(board)

            if check_win(board, current_player):
                print(f"Congratulations, Player {current_player}! You win!")
                game_on = False
            elif check_tie(board):
                print("It's a tie!")
                game_on = False
            else:
                current_player = "O" if current_player == "X" else "X"
        except (IndexError, ValueError):
            print("Invalid input. Please choose a number between 1 and 9.")

if __name__ == "__main__":
    tic_tac_toe()
