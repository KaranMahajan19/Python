def Addition(Value1,Value2):
	Ans = Value1 + Value2
	return Ans

def main():   						# Block
	print("Enter First No : ")
	no1 = int(input())

	print("Enter Second No : ")
	no2 = int(input())
	
	Sum = Addition(no1,no2)

	print("Addition is : ",Sum)	  # Block
if __name__ == "__main__":
	main()

