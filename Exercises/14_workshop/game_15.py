import random
from pyfiglet import Figlet


def gameplay():
    tries = 0
    if auto_mode == "Y":
        while game_list != list(range(1, list_length + 1)):
            print("***Автоматично разбъркване. Модерна работа.***")
            random.shuffle(game_list)
            tries += 1
            print(*game_list, sep=' | ')
    else:
        while game_list != list(range(1, list_length + 1)):
            enter = input("Натисни 'Enter' за да разбъркаш.")
            random.shuffle(game_list)
            tries += 1
            print(*game_list, sep=' | ')
    print(f"\nЧестито! Успя след {tries} опита. Печелиш {random_reward()}!\n")


def print_game_name():
    figlet = Figlet(font='poison')
    print(figlet.renderText("GAME 15"))


def define_rules():
    list_length_f = 0
    while True:
        try:
            list_length_f = int(input("Въведи дължината на листа: "))
            break
        except ValueError:
            print("Число, човече...")
            continue

    while True:
        auto_mode_f = input("Искаш ли да играеш с автоматичен режим? (Y/N): ").upper()
        if auto_mode_f not in ["Y", "N"]:
            print("Само 'Y' или 'N'. Не е трудно...")
            continue
        break
    if auto_mode_f == "Y":
        print("Ебаси мързела...")
    return list_length_f, auto_mode_f


def random_reward():
    rewards = [
        "дъвка с косъм",
        "загуба на време",
        "ваучер за поправка в Софтуни",
        "усмивка по радиото",
        "пожелание от Божинката",
        "капачка с надпис 'Опитай пак'"
    ]
    return random.choice(rewards)


print_game_name()

while True:
    list_length, auto_mode = define_rules()
    game_list = list(range(1, list_length + 1))
    random.shuffle(game_list)
    gameplay()
    answer = input("Играе ли ти се отново тази невероятно сложна игра? (Y/N): ").upper()
    while answer not in ["Y", "N"]:
        answer = input("Само 'Y' или 'N' бе човек... (Y/N): ").upper()
    if answer == "Y":
        continue
    print("Край на играта.")
    break

# Вдъхновена от легендарната игра от замунда - "Игра 15"
