import re
pattern = re.compile(r'[A-Za-z\']+')

with open('input.txt', 'r') as file:
    list_of_words = [x.casefold() for x in re.findall(pattern, "".join(file.readlines()))]
with open('words.txt', 'r') as file:
    word_count_dict = {word: list_of_words.count(word) for word in file.read().split()}
with open('output.txt', 'w') as file:
    for word, count in sorted(word_count_dict.items(), key=lambda x: -x[1]):
        file.write(f"{word} - {count}\n")


# 5.	Word Count
# Write a program that reads a list of words from the file words.txt and finds how many times each of the words is contained in another file text.txt. Matching should be case-insensitive.
# The results should be written to other text files. Sort the words by frequency in descending order.
# Examples
# words.txt	input.txt	output.txt
# quick is fault
# 	-I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here…It is safer.	is - 3
# quick - 2
# fault - 1