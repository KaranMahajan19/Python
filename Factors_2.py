
def main():

	print("Application to demonstration of Factor's")

	print("Enter a number : ")
	No = int(input())

	print("Factors are : ")

	i = 1

	while (i <= (No/2)):
		if ((No % i) == 0):
			print(i)
		i += 1

if __name__=="__main__":

	main()