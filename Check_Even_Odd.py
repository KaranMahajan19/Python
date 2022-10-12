############################################################
#	Program which to demonstrate the number is Even or Odd.
############################################################

def ChkNum(number):
	if (number % 2 == 0):
		print(number," Is Even number")
	else:
		print(number," : Is Odd number")

if __name__ == "__main__":

	print("Enter number that you check Even or Odd : ")
	No = int(input())
	ChkNum(No)

############################################################
#	Input : 2			Output : 2 Is Even number
#	Input : 3			Output : 3 Is Odd number
############################################################
