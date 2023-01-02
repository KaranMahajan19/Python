
def main():

	print("Application to demonstration of Factor's")

	print("Enter a number : ")
	No = int(input())

	print("Factor's are : ")
	for i in range(1,int(No/2)+1,1):
		if (No % i) == 0:
			print(i,end="	")

if __name__=="__main__":

	main()