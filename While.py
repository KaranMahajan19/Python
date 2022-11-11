#############################################################################
#	Demonstration of Displaying Numbers using while loop.
#############################################################################

def main():
	print("Enter how many numbers you want to display : ")
	Size = int(input())

	print("Numbers are : ")
	i = 1
	while(i <= Size):
		print(i)
		i = i + 1

if __name__=="__main__":
	main()

#############################################################################
#	Input 	:	Enter how many numbers you want to display :
#				5
#	Output	:	Numbers are :
#				1
#				2
#				3
#				4
#				5
#############################################################################