import os


def file_manipulator(command_f: list):
    file_name = command[1]

    def create():
        with open(file_name, 'w') as file:
            file.write('')

    def replace():
        try:
            with open(file_name, 'r') as file:
                text = file.read().replace(command[2], command[3])
            with open(file_name, 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    def add():
        with open(file_name, 'a') as file:
            file.write(f"{command[2]}\n")

    def delete():
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    commands = {
        'Create': lambda x: create(),
        'Add': lambda x: add(),
        'Replace': lambda x: replace(),
        'Delete': lambda x: delete()
    }
    return commands[command_f[0]]



command = input()
while command != 'End':
    command = command.split('-')
    file_manipulator(command)
    command = input()