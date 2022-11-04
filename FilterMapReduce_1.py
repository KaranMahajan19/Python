###############################################################
#   Map,mapX 	: return Addition of Number of list by 10
#	filterX 	: filter numbers in list between <70 or >90
#	reduceX		: return multiplication of all numbers in list 
###############################################################

def Map(No):
	return No + 10

def filterX(Filt):
	Result = []
	for i in Filt:
		if i >= 70	<= 90:
			Result.append(i)
	return Result

def mapX(DataM,Incr):
	Result = []
	for No in DataM:
		Value = Incr(No)
		Result.append(Value)
	return Result

def reduceX(DataM):

	Ans = 1
	for i in DataM:
		Ans	 = Ans * i
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
	List_Filter = filterX(Data)
	print("List after filter : ",List_Filter)

	List_Map = mapX(List_Filter,Map)
	print("List after map : ",List_Map)

	List_Reduce = reduceX(List_Map)
	print("List after reduce : ",List_Reduce)

if __name__ == "__main__":
	main()




#############################################################
#
#	Input List :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#	List after filter :  [76, 89, 86, 90, 70]
#	List after map :  [86, 99, 96, 100, 80]
#	List after reduce :  6538752000
#
#############################################################