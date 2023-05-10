#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    weka = "is negative"
elif number > 0:
    weka = "is positive"
else:
    weka = "is zero"
print("{:d}".format(number), weka)
