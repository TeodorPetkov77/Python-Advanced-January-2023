try:
    data = open('numbers.txt', 'r')
    print(sum([int(x) for x in data]))
except FileNotFoundError as err:
    print(err)

# 2.	File Reader
# You are given a file called numbers.txt with the following content:
# 1
# 2
# 3
# 4
# 5