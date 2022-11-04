##############################################################
#   Program which contains one lambda function which accepets 
#     one parameter and return power of two.
##############################################################


result = lambda No : 2 ** No

def main():
    print("Enter a number : ")
    No = int(input())

    Ans = result(No)
    print(No,"raise to power of two is :",Ans)

if __name__ == "__main__":
    main()


#############################################################
# Input : 4       Output : 16
# Input : 6       output : 64
#############################################################