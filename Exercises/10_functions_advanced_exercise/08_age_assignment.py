def age_assignment(*args, **kwargs):
    args = list(args)
    result = []
    while args:
        name = args.pop()
        for key in kwargs.keys():
            if name[0] == key:
                kwargs[name] = kwargs.pop(key)
                break
    sorted_tuple = sorted(kwargs.items(), key=lambda x: x[0])
    for name, age in sorted_tuple:
        result.append(f"{name} is {age} years old.")
    return "\n".join(result)

# https://judge.softuni.org/Contests/Compete/Index/1839#7

# 8.	Age Assignment
# Create a function called age_assignment() that receives a different number of names and a different number of key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number (age). Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in the format: "{name} is {age} years old."
# Submit only the function in the judge system.
# Examples
# Test Code	Output
# print(age_assignment("Peter", "George", G=26, P=19))	George is 26 years old.
# Peter is 19 years old.
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))	Amy is 22 years old.
# Bill is 61 years old.
# Willy is 36 years old.