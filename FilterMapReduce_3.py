#################################################################
#	ChkEven,filterX 	: filter Even numbers in list
#   Map,mapX 			: return Squares of all Numbers in list
#	reduceX				: return Addition of all numbers in list 
#################################################################

def filterX(DataM):
	i = 0
	Flag = True
	for i in range(2,int(DataM/2)+1):
		if(DataM % i == 0):
			Flag = False
			break
	return Flag

def main():

	print("Enter number of elements : ")
	No = int(input())

	print("Input elements")
	Data = []
	for i in range(0,No,1):
		No = int(input())
		Data.append(No)

	print("Input List : ",Data)

	List_Filter = filterX(Data)
	print("List after filter : ",List_Filter)


if __name__ == "__main__":
	main()




#############################################################
#
#	Input List :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#	List after filter :  [2, 4, 4, 2, 8, 10]
#	List after map :  [4, 16, 16, 4, 64, 100]
#	List after reduce :   204
#
#############################################################