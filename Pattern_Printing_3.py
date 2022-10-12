##########################################################################
# Application which accept one number and display pattern. 
##########################################################################

def No_Pattern():
     
    print("Enter number : ")
    No = int(input())
 
    num = 1
    for i in range(0, No):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\t")
 
# Driver code
#n = 5
#numpat(n)

if __name__=="__main__":

	No_Pattern()
############################################################
'''
Input  : 	5
Output :    1
			1 2
			1 2 3
			1 2 3 4
			1 2 3 4 5
'''
############################################################