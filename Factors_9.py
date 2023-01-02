from Fact_Module import Display_Factors as Num
from sys import argv

def main():

	print("Application to demonstration of factor's")

	print("Name of application is : ",argv[0])
	
	Num(int(argv[1]))	

if __name__=="__main__":

	main()