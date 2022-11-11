#############################################################################
#	Demonstration of Displaying Factors using Module
#############################################################################

#import FactorsModule

#from FactorsModule import DisplayFactors

#import FactorsModule as Fact

from FactorsModule import *
 
def main():

	print("Enter number that you to find factors : ")
	No = int(input())

	#FactorsModule.DisplayFactors(No)

	#DisplayFactors(No)

	#Fact.DisplayFactors(No)

	DisplayFactors(No)

if __name__=="__main__":
	main()

#############################################################################
#	Inout	:	Enter number that you to find factors :
#				10
#	Output	:	Factors are :
#				1       2       5
#############################################################################