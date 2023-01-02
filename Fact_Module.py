
def Display_Factors(Number):

	print("Factor's are : ")

	i = 1

	while (i <= int(Number/2)):
		if ((Number % i) == 0):
			print(i)
		i += 1