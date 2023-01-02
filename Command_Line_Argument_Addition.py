
from sys import *

def Addition(No1, No2):

	Ans = 0

	Ans = No1 + No2

	return Ans

def main():

	print("-Application to demonstration of Addition by Command Line Argument's-")

	print("Welcome to : ",argv[0])

	print("----------------------------------------------------------------")
	
	if(len(argv) == 2):
		
		if((argv[1] == "--U") or (argv[1] == "--u")):
			print("Use of application as : ")
			print("Python Name_of_Application First_Number Second_Number")
			print("For more help type '--H'")
			print("----------------------------------------------------------------")
			exit()

		if((argv[1] == "--H") or (argv[1] == "--h")):
			print("Help : ")
			print("This application is used to perform addition of 2 numbers")
			print("----------------------------------------------------------------")
			exit()

	if(len(argv) != 3):
		print("Invalid number of arguments")
		print("Please type '--U' to get the use application")
		print("----------------------------------------------------------------")
		exit()

	Ret = Addition(int(argv[1]), int(argv[2]))

	print("Addition is : ",Ret)

	print("Thank you for use Application")

	print("*******By Karan Mahajan*******")

	print("----------------------------------------------------------------")

if __name__=="__main__":

	main()