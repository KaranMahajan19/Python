
from Add_Module import Addition

def main():

	print("Demonstration of Addition of two numebrs")

	print("Enter first number : ")
	No1 = int(input())

	print("Enter second number : ")
	No2 = int(input())

	AddX = Addition(No1,No2)

	print("AdditionX is : ",AddX)

if __name__=="__main__":
	main()