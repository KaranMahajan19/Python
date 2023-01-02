
from sys import *

print("------Karan Mahajan------")
print("Demonstration of Command Line Argument's")

print("Name of Application is : ",argv[0])

print("Name of Module is : ",__name__)

X = int(argv[1])
Y = int(argv[2])

Addition = X + Y

print("Addition is : ",Addition)

# Input : Python NameOFApplication.py 10 20