#############################################################
#   Program which which accepts input nd store into list and
#       return Minimum number in list.
#############################################################

def Minimum(Value1,Value2):
    min = Value2[0]
    for i in range (len(Value2)):
        if Value2[i] < min:
            min = Value2[i]
    return min

def main():
    print("Number of elements : ")
    No = int(input())

    Data_Input = []

    print("Input elements : ")
    for i in range(0,No,1):
        InpEle = int(input())
        Data_Input.append(InpEle)

    Ans = Minimum(InpEle,Data_Input)
    print("Minimum number of list is : ",Ans)

if __name__ == "__main__":
    main()





############################################################
#   Number of elements : 4
#   Input elements : 13, 5, 45, 7
#   Output  :   5
############################################################