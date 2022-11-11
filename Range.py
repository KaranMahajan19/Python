########################################################
#	Demonstration of Range function
########################################################

def Range():
	print("Display 5 by displacemnt of 1 : ")
	for i in range(1,5+1):
		print(i)

	print("Display 10 numbers by displacemnt of 2 : ")
	for i in range(1,10,2):
		print(i)

def main():
	Range()

if __name__=="__main__":
	main()

########################################################
#	Output	:	Display 5 by displacemnt of 1 : 
#				1
#				2
#				3
#				4
#				5
#				Display 10 numbers by displacemnt of 2 : 
#				1
#				3
#				5
#				7
#				9
########################################################