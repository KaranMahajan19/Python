##########################################################################
# Application which accept input to display number pattern.
##########################################################################

def No_Pattern():
     
    print("Enter a number : ")
    No = int(input())

    for i in range(0,No):
        for j in range(0,No):
            print(j+1,end="    ")
        print()

if __name__=="__main__":

	No_Pattern()
############################################################
'''
Input  : 	5
Output :    1    2    3    4    5
            1    2    3    4    5
            1    2    3    4    5
            1    2    3    4    5
            1    2    3    4    5 
'''
############################################################
