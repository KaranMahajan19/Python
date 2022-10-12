##########################################################################
# Application which accept input to display "*" pattern. 
##########################################################################

def pattern():
     
    print("Enter number : ")
    No = int(input())
    b = 0
    # reverse for loop from 5 to 0
    for i in range(No, 0, -1):
        b += 1
        for j in range(1, i + 1):
            print("*", end="    ")
        print("\t")

if __name__=="__main__":

	pattern()
############################################################
'''
Input  : 	5
Output :    *    *    *    *    *
            *    *    *    *
            *    *    *
            *    *
            *   
'''
############################################################
