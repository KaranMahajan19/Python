
from sys import *

def main():

	print("Application to demonstration of Command Line Arguments")

	print("Name of Application : ",argv[0])

	print("First argument is : ",argv[1])

	print("Second argument is : ",argv[2])

	print("Third argument is : ",argv[3])

	print("Total argument is : ",len(argv))

if __name__=="__main__":

	main()