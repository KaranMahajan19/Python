print("Application to demonstrate Industrial Programming")

#####################################################
'''
# step1 :
print("Addition is : ",10+20)
'''
#####################################################
'''
# step2 :
no1 = 10
no2 = 20
Ans = no1 + no2
print("Addition is : ",Ans)
'''
#####################################################
'''
# step3 :

def main():
	no1 = 10
	no2 = 20
	Ans = no1 + no2

	print("Addition is : ",Ans)
main()
'''
#####################################################
'''
# step4 :

def main():					# Block
	no1 = 10
	no2 = 20
	Ans = no1 + no2

	print("Addition is : ",Ans)	  # Block

if __name__ == "__main__":
	main()
'''
#####################################################
'''
def main():					# Block
	print("Enter First No : ")
	no1 = input()

	print("Enter Second No : ")
	no2 = input()

	Ans1 = int(no1) + int(no2)

	print("Addition is : ",Ans)	  # Block
if __name__ == "__main__":
	main()
'''
'''
######################################################
def Addition(Value1,Value2):
	Ans = Value1 + Value2
	return Ans

def main():   						# Block
	print("Enter First No : ")
	no1 = input()

	print("Enter Second No : ")
	no2 = input()
	
	Ans = Addition(int(no1),int(no2))

	print("Addition is : ",Ans)	  # Block
if __name__ == "__main__":
	main()
'''
######################################################
'''
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
'''
#######################################################

print("Application to demonstrate Industrial programming")

import AdditionModule

def Addition(Value1,Value2):
    print("Value of __name__ from Addition is : ",__name__)
    Ans = Value1 + Value2
    return Ans

def main():
    print("Value of __name__ from main is : ",__name__)

    print("Enter first number : ")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    Sum = AdditionModule.Addition(no1,no2)

    print("Addition is : ",Sum)

if __name__ == "__main__":
    main()