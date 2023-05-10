#!/usr/bin/python3
finStr = ", "

for i in range(0, 100):
    if i == 99:
        finStr = ""
    print("{:02d}".format(i), end=finStr)
print('')
