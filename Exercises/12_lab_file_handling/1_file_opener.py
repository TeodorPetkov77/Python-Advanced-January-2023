try:
    file_to_open = open("text.txt", 'r')
    print("File found")
except FileNotFoundError:
    print("File not found. Creating file.")
    file_to_open = open("text.txt", 'w')

# 1.	File Opener
# You are given a file called text.txt with the following text:
# This is some random line
# This is the second line
# And this is the third one