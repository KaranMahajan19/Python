import sys

print("------Karan Mahajan------")
print("Demonstration of Command Line Argument's")

print("Name of Application is : ",sys.argv[0])

print("Name of Module is : ",__name__)

X = int(sys.argv[1])
Y = int(sys.argv[2])

Addition = X + Y

print("Addition is : ",Addition)

# Input : Python NameOFApplication.py 10 20