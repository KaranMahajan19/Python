##############################################################
#   Program which contains one lambda function which accepets 
#     two parameter and return it's multiplication.
##############################################################


result = lambda No,iNo : No * iNo

def main():
    print("Enter first number : ")
    No = int(input())

    print("Enter second number : ")
    iNo = int(input())

    Ans = result(No,iNo)
    print(No,"raise to power of two is :",Ans)

if __name__ == "__main__":
    main()


#############################################################
# Input : 4     3       Output : 12
# Input : 6     3       output : 18
#############################################################