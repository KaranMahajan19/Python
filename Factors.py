#############################################################################
#	Demonstration of Displaying Factors
#############################################################################

def While(Value):
	print("Factors using while are : ")
	i = 1
	while(i <= int(Value/2)):
		if(Value % i == 0):
			print(i)
		i = i + 1

def Range(Value):
	print("Factors using range are : ")
	for i in range(1,int(Value/2)+1,1):
		if(Value % i == 0):
			print(i)

def main():
	
	print("Enter number that want to display factors : ")
	No = int(input())

	While(No)

	Range(No)	

if __name__=="__main__":
	main()


#############################################################################
#	Input	:	Enter number that want to display factors :
#				10
#	Output	:	Factors using while are :
#				1
#				2
#				5
#				Factors using range are :
#				1
#				2
#				5
#############################################################################