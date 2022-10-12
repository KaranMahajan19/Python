##########################################################################
# Application which accept input and number is check prime or not.
##########################################################################

from math import sqrt

# Number to be checked for prime
def main():
	
	print("Enter a number : ")
	No = int(input())

	flag = 0

	if(No > 1):
		for k in range(2, int(sqrt(No)) + 1):
			if (No % k == 0):
				flag = 1
			break
		if (flag == 0):
			print(No,"is a Prime Number")
		else:
			print(No,"is Not a Prime Number")
	else:
		print(No,"is Not a Prime Number")

if __name__=="__main__":
	main()

############################################################
'''
Input  : 	5
Output :    5 is a Prime Number
'''
############################################################