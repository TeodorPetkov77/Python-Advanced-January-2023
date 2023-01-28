def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    elif word[index] != word[-index - 1]:
        return f"{word} is not a palindrome"
    else:
        return palindrome(word, index + 1)

# https://judge.softuni.org/Contests/Compete/Index/1839#8

# 9.	Recursion Palindrome
# Write a recursive function called palindrome() that will receive a word and an index (always 0). Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.
# Examples
# Test Code	Output
# print(palindrome("abcba", 0))	abcba is a palindrome
# print(palindrome("peter", 0))	peter is not a palindrome