#################################################################
#	ChkEven,filterX 	: filter Even numbers in list
#   Map,mapX 			: return Squares of all Numbers in list
#	reduceX				: return Addition of all numbers in list 
#################################################################

def ChkEven(EvNo):
	return (EvNo % 2 == 0)

def Map(SqNo):
	return SqNo ** 2

def filterX(Even,DataM):
	Result = []
	for i in DataM:
		if (Even(i) == True):
			Result.append(i)
	return Result

def mapX(DataM,Sqr):
	Result = []
	for No in DataM:
		Value = Sqr(No)
		Result.append(Value)
	return Result

def reduceX(DataM):

	Ans = 0
	for i in DataM:
		Ans	 = Ans + i
	return Ans

def main():

	print("Enter number of elements : ")
	No = int(input())

	print("Input elements")
	Data = []
	for i in range(0,No,1):
		No = int(input())
		Data.append(No)

	print("Input List : ",Data)
	List_Filter = filterX(ChkEven,Data)
	print("List after filter : ",List_Filter)

	List_Map = mapX(List_Filter,Map)
	print("List after map : ",List_Map)

	List_Reduce = reduceX(List_Map)
	print("List after reduce : ",List_Reduce)

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