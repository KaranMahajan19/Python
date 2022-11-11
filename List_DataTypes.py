########################################################
#	Demonstration of Sequence data type List
########################################################

def ListTraversal(Values):
	
	print("Value of index 0 : ",Values[0])
	print("Data type of index 0 : ",type(Values[0]))
	
	print("Value of index 1 : ",Values[1])
	print("Data type of index 1 : ",type(Values[1]))
	
	print("Value of index 2 : ",Values[2])
	print("Data type of index 2 : ",type(Values[2]))
	
	print("Value of index 3 : ",Values[3])
	print("Data type of index 3 : ",type(Values[3]))
	
	print("Value of index 4 : ",Values[4])
	print("Data type of index 4 : ",type(Values[4]))

def Range(Values):
	for i in range(0,len(Values),1):
		print(Values[i])

def main():

	List = [10,30,"Karan",83.80,True]

	print("Values of list using index : ")
	ListTraversal(List)

	print("length of list using range : ")
	Range(List)
	print("Length of list is : ",len(List))
	print("Data type of list is : ",type(List))

if __name__=="__main__":
	main()

########################################################
#	Output	:	Values of list using index :
#				Value of index 0 :  10
#				Data type of index 0 :  <class 'int'>
#				Value of index 1 :  30
#				Data type of index 1 :  <class 'int'>
#				Value of index 2 :  Karan
#				Data type of index 2 :  <class 'str'>
#				Value of index 3 :  83.8
#				Data type of index 3 :  <class 'float'>
#				Value of index 4 :  True
#				Data type of index 4 :  <class 'bool'>
#				length of list using range :
#				10
#				30
#				Karan
#				83.8
#				True
#				Length of list is :  5
#				Data type of list is :  <class 'list'>
########################################################