########################################################
# Demonstration of Command Line Arguments
########################################################

import sys

def main():

	print("Name of Application is : ",sys.argv[0])
	print("Special variable of __name__ from",__name__)

	Input1 = int(sys.argv[1])
	Input2 = int(sys.argv[2])

	Addition = Input1 + Input2
	print("Addition is : ",Addition)

if __name__=="__main__":
	main()

########################################################
#
#	Input  : python name.py 10 20
#	Output : Name of Application is : Name.py
#		   : Addition is : 30
#
########################################################
