#################################################################
#	Write a programm to check divisible by 5 or not
############################################################

def main(iNo):

	if (iNo % 5 == 0):
		print("True")
	else:
		print("False")

if __name__ == "__main__":
	
	print("Enter a Number : ")
	No = int(input())
	main(No)

############################################################
'''
Input  : 8
Output : False

Input : 25
Output : True

'''
############################################################