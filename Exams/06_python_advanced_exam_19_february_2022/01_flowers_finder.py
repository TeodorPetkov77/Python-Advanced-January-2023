from collections import deque


def check_word(words_dict_f, vowel_f, consonant_f, word_found_f):
    for key, value in words_dict_f.items():
        words_dict_f[key] = words_dict_f[key].replace(vowel_f, "")
        words_dict_f[key] = words_dict_f[key].replace(consonant_f, "")
        if not words_dict_f[key]:
            word_found_f = True
            print(f"Word found: {key}")
            break
    return words_dict_f, word_found_f


words_dict = {
    "rose": "rose",
    "lotus": "lotus",
    "daffodil": "daffodil",
    "tulip": "tulip"
}
vowels = deque(input().split())
consonants = input().split()


word_found = False


while vowels and consonants and not word_found:
    vowel = vowels.popleft() if vowels else ""
    consonant = consonants.pop() if consonants else ""
    words_dict, word_found = check_word(words_dict, vowel, consonant, word_found)

if not word_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

# https://judge.softuni.org/Contests/Practice/Index/3374#0

# 01.	Flower Finder
# You will be given two sequences of characters, representing vowels and consonants. Your task is to start checking if the following words could be found:
# •	"rose"
# •	"tulip"
# •	"lotus"
# •	"daffodil"
# Start by taking the first character of the vowels collection and the last character from the consonants collection. Then check if these letters are present in one or more of the given words. If a letter is present, that part of the word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple of letters until you find one of the given words above.
# A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:
# •	The letter "o" is present in "rose", "lotus", and "daffodil".
# •	The letter "l" is present in "tulip", "lotus", and "daffodil".
# •	The letter "f" is present in the word "daffodil" twice.
# The consonant and the vowel are always removed from the collection after trying to match them with the letters in the given words (whether successful or not). In the end, the program stops when a word is found, or there are no more vowels or consonants.
# As a result, if you found a word, print it and the remaining letters in each collection in the format described below. Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the format described below.
# Look at the provided examples for a better understanding of the problem.
# Input
# •	On the first line, you will receive vowels, separated by a single space (" ").
# •	On the second line, you will receive consonants, separated by a single space (" ").
# Output
# •	On the first line:
# o	If a word is found, print it in the format: "Word found: {word_found}"
# o	Otherwise, print: "Cannot find any word!"
# •	On the next lines, print the remaining letters in each collection (if there are any left):
# o	"Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
# o	"Consonants left: {consonants_one} {consonants_two} … {consonants_N}"
# Constraints
# •	All letters will be lowercase.
# •	The letter 'y' will always be a vowel.
# •	The letter 'w' will always be a consonant.
#
# Examples
# Input	Output
# o e a o e a i
# p r s x r	Word found: rose
# Vowels left: o e a i
# Consonants left: p r
# Comment
# Start by taking the first volew "o" and the last consonant "r". They are found in words "rose", "lotus", and "daffodil".
# Then, take "e" and "x". They are found in thr word "rose".
# Then, take "a" and "s". They are found in words "rose", "lotus", and "daffodil".
# The word "rose" is found, so we print it. Then we print the remaining letters in each sequence.
#
# Input	Output
# a a a
# x r l t p p	Cannot find any word!
# Consonants left: x r l
# u a o i u y o e
# p m t l	Word found: tulip
# Vowels left: u y o e