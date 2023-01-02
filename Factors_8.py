from Fact_Module import Display_Factors as Num
import sys

def main():

	print("Application to demonstration of factor's")

	print("Name of application is : ",sys.argv[0])
	
	Num(int(sys.argv[1]))	

if __name__=="__main__":

	main()