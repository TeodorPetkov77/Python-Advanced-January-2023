def even_odd_filter(**numbers):
    def odd_filter(key):
        numbers[key] = [x for x in numbers[key] if x % 2 != 0]
        return numbers[key]

    def even_filter(key):
        numbers[key] = [x for x in numbers[key] if x % 2 == 0]
        return numbers[key]

    for num_key, num_value in numbers.items():
        if num_key == "odd":
            numbers[num_key] = odd_filter(num_key)
        else:
            numbers[num_key] = even_filter(num_key)
    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))

# https://judge.softuni.org/Contests/Compete/Index/1839#3

# 4.	Numbers Filter
# Create a function called even_odd_filter() that can receive a different number of named arguments. The keys will be "even" and/or "odd", and the values will be a list of numbers.
# When the key is "odd", you should extract only the odd numbers from its list. When the key is "even", you should extract only the even numbers from its list.
# The function should return a dictionary sorted by the length of the lists in descending order. There will be no case of lists with the same length.
# Submit only your function in the judge system.
# Example
# Input	Output
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))	{'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))	{'odd': [5]}
