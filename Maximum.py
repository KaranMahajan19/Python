
def Maximum(Value1, Value2):

	if Value1 > Value2:
		return Value1
	else:
		return Value2

def main():

	print("Application to demonstrate to findout maximum number.")

	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	Max = Maximum(No1, No2)

	print("Maximum number is : ",Max)

if __name__=="__main__":
	main()