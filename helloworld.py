#!/usr/bin/python

from random import random

print("Alex")
numberOne = int(round(random() * 100))
numberTwo = int(round(random() * 100))
print(numberOne)
print(numberTwo)
print("Sum = " + str(numberOne + numberTwo))
print("Average = " + str(float(numberOne + numberTwo)/2))
