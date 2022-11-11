########################################################
#	Demonstration of Minimum number
########################################################

def Minimum(No1,No2):
	if No1 < No2:
		return No1
	else:
		return No2

def main():

	print("Enter first number : ")
	Input1 = int(input())

	print("Enter second number : ")
	Input2 = int(input())

	Ans = Minimum(Input1, Input2)
	print("Minimum number is : ",Ans)

if __name__=="__main__":
	main()

########################################################
#	Input   : 	Enter first number :
#				10
#				Enter second number :
#				20
#	Output	:	Minimum number is :  10
########################################################