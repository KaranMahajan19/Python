##########################################################################
# Application which accept one number and return number of digits in that 
#    number
##########################################################################

def Digits():
     
    print("Enter a number : ")
    No = int(input())
    
    Ans = 0
    while(No>0):
        digits = No % 10
        Ans = Ans + digits
        No = No // 10
    print(Ans)

if __name__=="__main__":

	Digits()
    
############################################################
'''
Input  : 	5187934
Output :    37
'''
############################################################