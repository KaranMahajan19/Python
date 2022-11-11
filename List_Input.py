########################################################
#	Demonstration of List Input
########################################################

def main():

	List = []

	print("Enter how many Elements you want to store : ")
	Size = int(input())

	print("Enter Elements : ")
	for i in range(0,Size):
		Elements = input()
		List.append(Elements)

	print(List)

if __name__=="__main__":
	main()

####################################################################################
#	Input	:	Enter how many elements you want to store :
#				5
#				Enter elements :
#				Created
#				By
#				Karan
#				Mahajan
#				@Mahajankaran19@gmail.com
#	Output	:	['Created', 'By', 'Karan', 'Mahajan', '@Mahajankaran19@gmail.com']
####################################################################################