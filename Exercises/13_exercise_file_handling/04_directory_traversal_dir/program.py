import os
from os.path import isfile

file_names = [x for x in os.listdir() if isfile(x)]
print(file_names)