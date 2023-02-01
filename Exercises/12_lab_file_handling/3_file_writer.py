file_name = 'my_first_file.txt'
lines = ['this\n', 'is\n', 'a\n', 'list\n', 'of\n', 'text\n']
with open(file_name, 'w') as file:
    file.write('I just created my first file!\n')
    file.writelines(lines)
with open(file_name, 'r') as file:
    print(file.read())
with open(file_name, 'a') as file:
    file.write('You can also append to file.')
with open(file_name, 'r') as file:
    print(file.read())

# 3.	File Writer
# Create a program that creates a file called my_first_file.txt. In that file,
# write a single line with the content: 'I just created my first file!'