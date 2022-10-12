##########################################################################
# Application to display Addition, Subtraction, Multiplication, Division.
##########################################################################

def Arithmetic():
	def Add(iValue1,iValue2):
		Ans = iValue1 + iValue2
		return Ans

	def Sub(iValue1,iValue2):
		Ans = iValue1 - iValue2
		return Ans

	def Mul(iValue1,iValue2):
		Ans = iValue1 *	iValue2
		return Ans

	def Div(iValue1,iValue2):
		Ans = iValue1 / iValue2
		return Ans

	Addition = Add(iNo1,iNo2)
	print("Addition is : ",Addition)

	Subtraction = Sub(iNo1,iNo2)
	print("Subtraction is : ",Subtraction)

	Multiplication = Mul(iNo1,iNo2)
	print("Multiplication is : ",Multiplication)
	
	Division = Div(iNo1,iNo2)
	print("Division is : ",Division)

if __name__ == "__main__":

	print("Enter first number : ")
	iNo1 = int(input())

	print("Enter second number : ")
	iNo2 = int(input())

	Arithmetic()


############################################################
'''
Input  : 10, 20
Output : Addition is :  30
		 Subtraction is :  -10
		 Multiplication is :  200
		 Division is :  0.5
'''
############################################################