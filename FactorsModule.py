def DisplayFactors(Value):

	print("Factors are : ")
	
	i = 1
	while(i <= int(Value/2)):
		if(Value % i == 0):
			print(i, end="	")
		i = i + 1