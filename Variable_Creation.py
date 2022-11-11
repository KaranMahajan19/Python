###################################################################
#	application to Demonstration of local/global variable creation
###################################################################

# Global varibale
No = 21											
print("Value of Global variable No is : ",No)

def main():
	
	# Local variable
	Integer = 11
	Float = 83.80
	Boolean = True
	String = "Raver"

	print("Value of Global variable No is : ",No)
	
	print("Values : ")
	print("Value of Integer is : ",Integer)
	print("Value of Float is : ",Float)
	print("Value of Boolean is : ",Boolean)
	print("Value of String is : ",String)

	print("Data types : ")
	print("Data type of Integer is : ",type(Integer))
	print("Data type of Float is : ",type(Float))
	print("Data type of Boolean is : ",type(Boolean))
	print("Data type of String is : ",type(String))

	print("ID's : ")
	print("ID of Integer is : ",id(Integer))
	print("ID of Float is : ",id(Float))
	print("ID of Boolean is : ",id(Boolean))
	print("ID of String is : ",id(String))

	print("Multiple Variable create in one line")

	I, F, B, S = 11, 83.80, True, "Raver"
	print("Value of I is : ",I)
	print("Value of F is : ",F)
	print("Value of B is : ",B)
	print("Value of S is : ",S)

	print("Values of I, F, B, S : ",I, F, B, S)

if __name__=="__main__":
	main()


###############################################################
#
#	Output	:	Value of Global variable No is :  21
#				Value of Global variable No is :  21
#				Values :
#				Value of Integer is :  11
#				Value of Float is :  83.8
#				Value of Boolean is :  True
#				Value of String is :  Raver
#				Data types :
#				Data type of Integer is :  <class 'int'>
#				Data type of Float is :  <class 'float'>
#				Data type of Boolean is :  <class 'bool'>
#				Data type of String is :  <class 'str'>
#				ID's :
#				ID of Integer is :  140726698252272
#				ID of Float is :  2909700514864
#				ID of Boolean is :  140726697973584
#				ID of String is :  2909706314032
#				Multiple Variable create in one line
#				Value of I is :  11
#				Value of I is :  83.8
#				Value of I is :  True
#				Value of I is :  Raver
#				Values of I, F, B, S :  11 83.8 True Raver
#
###############################################################
