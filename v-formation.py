import sys
import time

name = sys.argv[1]

middle_space = 2 * len(name) - 3
begin = 0
counter = 1

for char in name:
    middle = middle_space * ' '
    if counter == len(name):
        print(begin * ' ' + char)
    else:
        print(begin * ' ' + char + middle + char)
    begin += 1
    middle_space -= 2
    counter += 1
    time.sleep(1)
print(name)