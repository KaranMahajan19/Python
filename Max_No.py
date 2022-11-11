########################################################
#	Demonstration of Maximum number
########################################################

def Maximum(No1,No2):
	if No1 > No2:
		return No1
	else:
		return No2

def main():

	print("Enter first number : ")
	Input1 = int(input())

	print("Enter second number : ")
	Input2 = int(input())

	Ans = Maximum(Input1, Input2)
	print("Maximum number is : ",Ans)

if __name__=="__main__":
	main()

########################################################
#	Input   : 	Enter first number :
#				10
#				Enter second number :
#				20
#	Output	:	Maximum number is :  20
########################################################