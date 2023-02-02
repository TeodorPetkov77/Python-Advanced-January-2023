file_name = 'text.txt'

with open(file_name, 'w') as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n"
               "-Is this some kind of joke?! Is it?\n"
               "-Quick, hide here. It is safer.")

symbols = ["-", ",", ".", "!", "?"]

with open(file_name, 'r') as file:
    for line, text in enumerate(file.read().split('\n')):
        if line % 2 == 0:
            final_text = []
            for index in range(len(text.split())-1, -1, -1):
                word = ''.join(['@' if x in symbols else x for x in text.split()[index]])
                final_text.append(word)
            print(" ".join(final_text))

# The above code splits the text in "text.txt" by new line "\n" and creates a list to iterate over each line.
# To work only with even lines I get the line number with the enumerate function and the "if line % 2 == 0" condition.
# Create an empty list (final_text) for the final text to append all corrected words in and later convert to string with ".join".
# Split each sentence to a list and iterate over it starting from the back.
# With a comprehension replace each symbol found in the "symbols" list with "@" and ".join" to convert word from list to string.
# Append each word to the final_text list and print the list as a string with "' '.join" when the loop is done.
# The condition is to print the required data and not change the initial file.

# --------------------------------------------------

# 1.	Even Lines
# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
# Examples
# text.txt	output
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.	fault@ his wasn't it but him@ judge to quick was @I
# safer@ is It here@ hide @Quick@