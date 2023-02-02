import os


def file_manipulator(command_f: list):
    action = command_f[0]
    file_name = command_f[1]

    def create():
        with open(file_name, 'w') as file:
            file.write('')

    def replace():
        try:
            with open(file_name, 'r') as file:
                text = file.read().replace(command_f[2], command_f[3])
            with open(file_name, 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    def add():
        with open(file_name, 'a') as file:
            file.write(f"{command_f[2]}\n")

    def delete():
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    commands = {
        'Create': create,
        'Add': add,
        'Replace': replace,
        'Delete': delete
    }
    commands[action]()


command = input()
while command != 'End':
    command = command.split('-')
    file_manipulator(command)
    command = input()


# Keep in mind that the file may not appear or disappear in the Project tab immediately upon executing a command. Open the folder and check there.


# 3.	File Manipulator
# Create a program that will receive commands until the command "End". The commands can be:
# •	"Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)
# •	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
# •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
# •	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
# Example
# Input	Comment
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End	The first command creates the empty file
# After the first and second Add command, the content is:
# First Line
# Second Line
# On the first Replace command, an error must occur
# After the next two Replace commands, the content is:
# 1st Line
# 2nd Line
# After the first Delete command, an error occurs
# Finally, the 'file.txt' file is deleted