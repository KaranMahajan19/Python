#############################################################
#   Program which which accepts input nd store into list and
#       return Maximum number in list.
#############################################################

def Maximum(Value1,Value2):
    Max = 0
    for No in Value2:
        if No > Max:
            Max = No
    return Max

def main():
    print("Number of elements : ")
    No = int(input())

    Data_Input = []

    print("Input elements : ")
    for i in range(0,No,1):
        MaxNo = int(input())
        Data_Input.append(MaxNo)

    Ans = Maximum(MaxNo,Data_Input)
    print("Maximum number of list is : ",Ans)

if __name__ == "__main__":
    main()


############################################################
#   Number of elements : 7
#   Input elements : 13, 5, 45, 7, 4, 56, 34
#   Output  :   56
############################################################