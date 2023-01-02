import Add_Module

def main():

	print("Demonstration of Addition of two numebrs")

	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	Add = Add_Module.Addition(No1, No2)

	print("Addition is : ",Add)

if __name__=="__main__":
	main()