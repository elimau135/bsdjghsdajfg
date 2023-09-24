import math

original_list = [6, 14, 8, 7, 10, 13, 1, 4, 3]

def sortList(): #function that sorts list form smallest to highest value
    for i in range(len(original_list)):
        for j in range(0, len(original_list)-i-1):
            if original_list[j]>original_list[j+1]:
                original_list[j], original_list[j+1] = original_list[j+1], original_list[j]

def splitList():
    sortList()
    length = len(original_list)
    indexSplitValue = math.ceil(length/2)
    i = 0 
    newList1 = []
    newList2 = []
    for i in range(length):
        if i < indexSplitValue:
            newList1.append(original_list[i])
    print(newList1)
    for i in range(length):
        if i > indexSplitValue:
            newList2.append(original_list[i])
    print(newList2)
            

splitList()
