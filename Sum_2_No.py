############################################################
#	Program which to demonstrate addition of two number's
############################################################


def Add(iValue1,iValue2):
	Ans = iValue1 + iValue2
	return Ans

def main():
	
	print("Enter first number : ")
	iNo1 = int(input())

	print("Enter second number : ")
	iNo2 = int(input())

	Sum = Add(iNo1,iNo2)

	print("Addition is : ",Sum)

if __name__ == "__main__":

	main()


############################################################
#	Input  : 11, 5
#	Output : 16
############################################################