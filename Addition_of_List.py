#############################################################
#   Program which which accepts input nd store into list and
#       return addition elements in list.
#############################################################

def Sum(A,B):
    return A + B

def Addition(Value1,Value2):
    Sum = 0
    for No in Value2:
        Sum = Sum + No
    return Sum

def main():
    print("Number of elements : ")
    No = int(input())

    Data_Input = []

    print("Input elements : ")
    for i in range(0,No,1):
        Add = int(input())
        Data_Input.append(Add)

    Ans = Addition(Add,Data_Input)
    print("Addition of list is : ",Ans)

if __name__ == "__main__":
    main()


############################################################
#   Number of elements : 6
#   Input elements : 13, 5, 45, 7, 4, 56
#   Output  :   130
############################################################