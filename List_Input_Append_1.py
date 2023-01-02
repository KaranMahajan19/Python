
def main():

	Arr = list()

	print("Enter how many elements you want to store ?")
	Size = int(input())

	print("Enter elements : ")

	for i in range(0,Size):
		no = int(input())
		Arr.append(no)
		#Arr.insert(i,no)

	print("List : ",Arr)

if __name__=="__main__":

	main()