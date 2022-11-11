############################################################
#	Demonstration of Command line arguments
############################################################

from sys import*

def main():
	
	print("Total number of arguments are : ",len(argv))
	print("Name of application is : ",argv[0])
	print("First argument is : ",argv[1])
	print("Second argument is : ",argv[2])
	print("Third argument is : ",argv[3])

if __name__=="__main__":
	main()


############################################################
#
#	Input	:	python CommandLineArg.py Karan 19 07
#	Output	:	Total number of arguments are :  4
#				Name of application is :  CommandLineArg.py
#				First argument is :  Karan
#				Second argument is :  19
#				Third argument is :  07
#
############################################################