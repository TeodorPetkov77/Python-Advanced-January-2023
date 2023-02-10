from collections import deque
from pyfiglet import Figlet


def check_for_win(row, col):
    look_for = players[0][1]

    def check_horizontal():
        if look_for * combination in "".join([x for x in board[row]]):
            return combination
        return 0

    def check_vertical():
        if look_for * combination in "".join([board[r][col] for r in range(len(board))]):
            return combination
        return 0

    def check_diagonal_1(row_f, col_f):
        symbols = 0
        while True:
            row_f += 1
            col_f -= 1
            if row_f not in range(len(board)) or col_f not in range(len(board[0])):
                break
        while True:
            row_f -= 1
            col_f += 1
            if row_f in range(len(board)) and col_f in range(len(board[0])):
                if board[row_f][col_f] == look_for:
                    symbols += 1
            else:
                break
        return symbols

    def check_diagonal_2(row_f, col_f):
        symbols = 0
        while True:
            row_f -= 1
            col_f -= 1
            if row_f not in range(len(board)) or col_f not in range(len(board[0])):
                break
        while True:
            row_f += 1
            col_f += 1
            if row_f in range(len(board)) and col_f in range(len(board[0])):
                if board[row_f][col_f] == look_for:
                    symbols += 1
            else:
                break
        return symbols

    return max(check_vertical(), check_horizontal(), check_diagonal_1(row, col), check_diagonal_2(row, col))


def next_player():
    players.append(players.popleft())


def print_board():
    print()
    [print(x) for x in board]
    print()


def gameplay():
    while True:
        chosen_column = choose_column_func() - 1
        row = 0
        if board[row][chosen_column] != "0":
            print(f"Column № {chosen_column} is full.")
            continue
        for row in (range(len(board))):
            if board[row][chosen_column] != "0":
                row -= 1
                board[row][chosen_column] = players[0][1]
                break
        else:
            board[row][chosen_column] = players[0][1]
        if check_for_win(row, chosen_column) == combination:
            print(f"\n{players[0][0]} Wins!!!\n")
            print("Final state of the game:")
            print_board()
            break
        print_board()
        next_player()


def choose_column_func():
    while True:
        try:
            chosen_column = int(input(f"{players[0][0]}, please choose a column from 1 to "
                                      f"{len(board[0])}: "))
            if not 1 <= chosen_column <= (len(board[0])):
                raise ValueError
            return chosen_column
        except ValueError:
            print("Invalid input.")


def create_matrix():
    figlet = Figlet(font='big')
    print(figlet.renderText("Connect 4"))
    while True:
        try:
            rows = int(input("Enter amount of rows for the board: "))
            cols = int(input("Enter amount of columns for the board: "))
            break
        except ValueError:
            print("Invalid input.")
    return [["0" for col in range(cols)] for row in range(rows)]


def define_name_and_rules():
    player_1_f = input("Player 1, please state your name: ")
    player_1_symbol_f = player_1_f[0]

    while True:
        player_2_f = input("Player 2, please state your name: ")
        if player_1_f == player_2_f:
            print("Name already taken.")
            continue
        player_2_symbol_f = player_2_f[0]
        while player_2_symbol_f == player_1_symbol_f:
            answer = input(f"Your symbol matches {player_1_f}'s symbol - '{player_1_symbol_f}'. "
                           f"Would you like to change it to something else? Enter Y or N: ").upper()
            if answer == "Y":
                player_2_symbol_f = input("Choose your own symbol (Must be 1 character long): ")
                while len(player_2_symbol_f) != 1:
                    player_2_symbol_f = input("Symbol must be 1 character long: ")
            elif answer == "N":
                print("Continuing with your current symbol.")
                break
        break

    while True:
        try:
            combination_f = int(input("Pick how many to connect for the win: "))
            break
        except ValueError:
            print("Invalid input.")

    players_f = deque([(player_1_f, player_1_symbol_f), (player_2_f, player_2_symbol_f)])

    return player_1_f, player_2_f, player_1_symbol_f, player_2_symbol_f, combination_f, players_f


def start_game():
    print()
    figlet = Figlet(font='alligator')
    print(figlet.renderText("Game start!"))
    answer = ""
    while True:
        gameplay()
        answer = input("Would you like to play again? Enter Y or N: ").upper()
        while answer not in ["Y", "N"]:
            answer = input("Sorry didn't quite catch that.")
        if answer == "Y":
            continue
        else:
            print("Game over.")
            break


board = create_matrix()
player_1, player_2, player_1_symbol, player_2_symbol, combination, players = define_name_and_rules()
start_game()

