from collections import deque
from pyfiglet import Figlet


def check_for_draw():
    list_of_o = [[x for x in row if x == "0"] for row in board]
    return [x for x in list_of_o if x]


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
    print(f"\n{[print(x) for x in board]}\n")



def gameplay():
    while True:
        chosen_column = choose_column_func() - 1
        row = 0
        if board[row][chosen_column] != "0":
            print(f"Column № {chosen_column + 1} is full.")
            continue
        for row in (range(len(board))):
            if board[row][chosen_column] != "0":
                row -= 1
                board[row][chosen_column] = players[0][1]
                break
        else:
            board[row][chosen_column] = players[0][1]
        if check_for_win(row, chosen_column) == combination:
            figlet = Figlet(font='poison')
            print(figlet.renderText("GAME OVER"))
            figlet = Figlet(font='big')
            print(figlet.renderText(f"{players[0][0]} Wins!\n"))
            break
        if not check_for_draw():
            figlet = Figlet(font='poison')
            print(figlet.renderText("GAME OVER"))
            figlet = Figlet(font='big')
            print(figlet.renderText("Draw! No one wins."))
            break

        print_board()
        next_player()

    print("Final state of the game:")
    print_board()


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
    while True:
        player_1_f = input("Player 1, please state your name: ")
        if len(player_1_f) == 0:
            print("Name cannot be blank.")
            continue
        player_1_symbol_f = player_1_f[0].upper()
        break
    while True:
        player_2_f = input("Player 2, please state your name: ")
        if len(player_2_f) == 0:
            print("Name cannot be blank.")
            continue
        if player_1_f == player_2_f:
            print("Name already taken.")
            continue
        player_2_symbol_f = player_2_f[0].upper()
        while player_2_symbol_f == player_1_symbol_f:
            answer_f = input(f"Your symbol matches {player_1_f}'s symbol - '{player_1_symbol_f}'. "
                             f"Would you like to change it to something else? (Y/N): ").upper()
            if answer_f == "Y":
                player_2_symbol_f = input("Choose your own symbol (Must be 1 character long): ").upper()
                while len(player_2_symbol_f) != 1:
                    player_2_symbol_f = input("Symbol must be 1 character long: ").upper()
            elif answer_f == "N":
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
    figlet = Figlet(font='big')
    print(figlet.renderText("GAME START!"))
    gameplay()


board = create_matrix()
player_1, player_2, player_1_symbol, player_2_symbol, combination, players = define_name_and_rules()

while True:
    start_game()
    answer = input("Would you like to play again? (Y/N): ").upper()
    while answer not in ["Y", "N"]:
        answer = input("Sorry didn't quite catch that. Play again? (Y/N): ").upper()
    if answer == "Y":
        answer = input("Would you like to reconfigure the names and rules?(Y/N): ").upper()
        while answer not in ["Y", "N"]:
            answer = input("Sorry didn't quite catch that. Reconfigure the names and rules?? (Y/N): ").upper()
        if answer == "Y":
            board = create_matrix()
            player_1, player_2, player_1_symbol, player_2_symbol, combination, players = define_name_and_rules()
        elif answer == "N":
            print("Continuing with current configuration.")
    elif answer == "N":
        break
