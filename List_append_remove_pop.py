############################################################
# Demonstration of function's append, insert, remove, pop
############################################################

def main():
	print("Demonstration of function append, insert, remove, pop")

	data = [11,21,51,101,21,11]			# Duplicate
	data1 = [11, 90.80, True, "Hello"]		# Heterogeneous

	print("Data is Heterogeneous : ",data1)
	print("Data is ordered : ",data1)
	print("Data at index 2 : ",data1[2])
	print("Data with duplicate elements : ",data)

	print("List is Mutable")
	data.append(201)
	
	print("Data after Append : ",data)

	data.insert(3,501)
	print("Data after Insert",data)
	data.remove(21)
	print("Data after Remove element",data)
	data.pop()
	print("Data after pop/remove last element : ",data)	

if __name__=="__main__":
	main()


##################################################################################
#	Output	:	Demonstration of function append, insert, remove, pop
#				Data is Heterogeneous :  [11, 90.8, True, 'Hello']
#				Data is ordered :  [11, 90.8, True, 'Hello']
#				Data at index 2 :  True
#				Data with duplicate elements :  [11, 21, 51, 101, 21, 11]
#				List is Mutable
#				Data after Append :  [11, 21, 51, 101, 21, 11, 201]
#				Data after Insert [11, 21, 51, 501, 101, 21, 11, 201]
#				Data after Remove element [11, 51, 501, 101, 21, 11, 201]
#				Data after pop/remove last element :  [11, 51, 501, 101, 21, 11]
##################################################################################