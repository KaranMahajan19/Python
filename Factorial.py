##########################################################################
# Application which accept input and display factorial of that input. 
##########################################################################

def factorial(iNo):

	if iNo == 1:
		return 1
	else:
		return (iNo * factorial(iNo-1))

	

if __name__ == "__main__":

	print("Enter a number : ")
	No = int(input())

	Ans = factorial(No)

	print("Factorial of",No,"is :",Ans)


############################################################
'''
Input  : 	5
Output :    Factorial of 5 is : 120
'''
############################################################