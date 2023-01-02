
def Append(Size):

	Arr = list()
	print("Enter elements : ")
	for i in range(0,Size):
		no = int(input())
		Arr.append(no)
	return Arr

def main():

	print("Enter how many elements you want to store ?")
	Size = int(input())

	Ans = Append(Size)
	print(Ans)

if __name__=="__main__":

	main()