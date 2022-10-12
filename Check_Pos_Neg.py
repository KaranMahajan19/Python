###################################################################
#	Write a programm to check number is positive, negative or zero
###################################################################

def main():
	print("Enter a Number : ")
	No = float(input())		# allowed to display intger as well as decimal degit
	
	#No = int(input())		# Not allowed to display decimal degit

	if No > 0:
		print("Number is Positive")
	elif No == 0:
		print("Zero")
	else:
		print("Number is Negative")

if __name__ == "__main__":
	main()

############################################################
'''
Input  : -1
Output : Number is negative

Input : 0
Output : Zero

Input : 1
Output : Number is posistive

Input  : -11.11
Output : Number is negative

Input : 0
Output : Zero

Input : 11.11
Output : Number is posistive

'''
############################################################