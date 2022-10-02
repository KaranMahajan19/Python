# Aplication to Findout Maximum number in between 3 number

def Maximum(No1, No2, No3):
	if (No1 >= No2):
		return No1
	elif (No2 >= No3):
		return No2
	else:
		return No3

def main():

	print("Enter first no : ")
	Value1 = input()
	
	print("Enter second no : ")
	Value2 = input()

	print("Enter third no : ")
	Value3 = input()

	Ans = Maximum(int(Value1),int(Value2),int(Value3))

	print("Maximum number is : ",Ans)

if __name__ == "__main__":
	main()
