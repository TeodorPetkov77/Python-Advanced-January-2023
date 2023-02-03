import os
from os.path import isfile, join

# Import isfile and join to allow work only with files and not dirs.
# join is a smart way to automatically join the path to the file with the file,
# since I wanted to work with a directory that's not the current one.

dir_name = '04_directory_traversal_dir'
all_file_names = [x for x in os.listdir(dir_name) if isfile(join(dir_name, x))]
file_dict = {}

# Create a list with only file names and an empty dictionary to fill later.

for file in all_file_names:
    extension = file.split(".")[1]
    name = file.split(".")[0]
    if extension not in file_dict:
        file_dict[extension] = []
    file_dict[extension].append(file)

# Fill in the dictionary with extensions as keys and list of files under each ext.

with open("report.txt", "w") as report:
    report.write("")

# Creates an empty file with "w" in order to reset it and delete the data every time the program is run.

for extension, files in sorted(file_dict.items()):
    with open("report.txt", "a") as report:
        report.write(f".{extension}\n")
    for file in files:
        with open("report.txt", "a") as report:
            report.write(f"- - - {file}\n")


# Fill in the data by going through the sorted dictionary.

# The program is meant to work with the files in "04_directory_traversal_dir".


# 4.	Directory Traversal
# Write a program that traverses a given directory for all files. Search through the first level of the directory only and write information about each found file in report.txt. The files should be grouped by their extension. Extensions should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.
# Examples
# Input	Directory View	report.txt
# .	 	.html
# - - - index.html
# .js
# - - - index.js
# .pptx
# - - - demo.pptx
# .py
# - - - program.py
# - - - python.py
# .txt
# - - - log.txt
# - - - notes.txt