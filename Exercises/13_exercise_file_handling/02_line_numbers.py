symbols = ["-", ",", ".", "!", "?", "'", ";", ":", "(", ")"]
file_name = 'text.txt'
text_to_append = ""

with open("output.txt", 'w') as output:
    output.write("")

# Creates an empty file with "w" in order to reset it and delete the data every time the program is run.

with open(file_name, 'r') as file:
    for line, sentence in enumerate(file.read().split('\n')):
        with open("output.txt", 'a') as output:
            output.write(f"Line {line + 1}: {sentence} "
                         f"({len([x for x in list(sentence) if x.isalpha()])})"
                         f"({len([x for x in list(sentence) if x in symbols])})\n")

# 2.	Line Numbers
# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and punctuation marks. The result should be written to another text file.
# Examples
# text.txt	output.txt
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.	Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# Line 2: -Is this some kind of joke?! Is it? (24)(4)
# Line 3: -Quick, hide here. It is safer. (22)(4)