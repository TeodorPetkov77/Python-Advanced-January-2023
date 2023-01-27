def concatenate(*args, **kwargs):
    final_string = "".join(list(args))
    for replace_string, new_string in kwargs.items():
        if replace_string in final_string:
            final_string = final_string.replace(replace_string, new_string)
    return final_string

# https://judge.softuni.org/Contests/Compete/Index/1839#4

# 5.	Concatenate
# Write a concatenate() function that receives some strings as arguments and some named arguments (the key will be a string, and the value will be another string).
# First, you should concatenate all arguments successively. Next, take each key successively, and if it is present in the resulted string, change all matching parts with the key's value. In the end, return the final string.
#  See the examples for more clarification.
# Submit only your function in the judge system.
# Examples
# Test Code	Output
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))	SoftUniIsGreat!
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))	I Love Python