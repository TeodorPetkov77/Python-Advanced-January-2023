import random
from pyfiglet import Figlet


def gameplay():
    tries = 0
    if auto_mode == "Y":
        while game_list != list(range(1, list_length + 1)):
            print("Auto shuffling. ***The future is here.***")
            random.shuffle(game_list)
            tries += 1
            print(*game_list, sep=' | ')
    else:
        while game_list != list(range(1, list_length + 1)):
            enter = input("Press Enter to shuffle.")
            random.shuffle(game_list)
            tries += 1
            print(*game_list, sep=' | ')
    print(f"Честито! Успя след {tries} опита. Печелиш {random_reward()}!")


def print_game_name():
    figlet = Figlet(font='poison')
    print(figlet.renderText("GAME 15"))


def define_rules():
    list_length_f = 0
    while True:
        try:
            list_length_f = int(input("Enter list length: "))
            break
        except ValueError:
            print("Invalid input.")
            continue

    while True:
        auto_mode_f = input("Would you like to enable auto mode? (Y/N): ").upper()
        if auto_mode_f not in ["Y", "N"]:
            print("Invalid answer.")
            continue
        break
    return list_length_f, auto_mode_f


def random_reward():
    rewards = [
        "дъвка с косъм",
        "загуба на време",
        "ваучер за поправка в Софтуни",
        "усмивка по радиото",
        "поздрав от Божинката (нищо)",
        "капачка с надпис 'Опитай пак'"
    ]
    return random.choice(rewards)


print_game_name()

while True:
    list_length, auto_mode = define_rules()
    game_list = list(range(1, list_length + 1))
    random.shuffle(game_list)
    gameplay()
    answer = input("Would you like to play again? (Y/N): ").upper()
    while answer not in ["Y", "N"]:
        answer = input("Invalid answer. Would you like to play again? (Y/N): ")
    if answer == "Y":
        continue
    print("Game Over.")
    break

# Вдъхновена от легендарната игра от замунда - "Игра 15"
