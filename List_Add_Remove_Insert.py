#############################################################################
#	Demonstration of List using append(), insert(), remove()
#############################################################################

def main():

	List = [19,"Karan",83.80,True]

	print("Data type of list is : ",type(List))
	
	print("Data type of '19' is : ",type(List[0]))
	print("Data type of 'Karan' is : ",type(List[1]))
	print("Data type of '83.80' is : ",type(List[2]))
	print("Data type of 'True' is : ",type(List[3]))

	print("Length of list is : ",len(List))
	print("Data is : ",List[0],List[1],List[2],List[3])

	List.append(2001)						# only one data can append
	print("after append data is : ",List)

	List.insert(1,21)						#(Index_NO, Data)
	print("after insert data is : ",List)

	List.remove(True)						# only one data can remove
	print("after remove data is : ",List)
	print("Length after operation on list is : ",len(List))


if __name__=="__main__":
	main()

#############################################################################
#
#	Output	:	Data type of list is :  <class 'list'>
#				Data type of '19' is :  <class 'int'>
#				Data type of 'Karan' is :  <class 'str'>
#				Data type of '83.80' is :  <class 'float'>
#				Data type of 'True' is :  <class 'bool'>
#				Data type of list is :  <class 'list'>
#				Length of list is :  4
#				Data is :  19 Karan 83.8 True
#				after append data is :  [19, 'Karan', 83.8, True, 2001]
#				after insert data is :  [19, 21, 'Karan', 83.8, True, 2001]
#				after remove data is :  [19, 21, 'Karan', 83.8, 2001]
#				Length after operation on list :  5
#
#############################################################################