
def bubbleSort(ary):
    # O(n^2) runtime
    k = 0
    j = len(ary) - 1
    while k < j:
        for i in range(0,j):
            if i+1 <= j:
                if ary[i] > ary[i+1]:
                    temp = ary[i]
                    ary[i] = ary[i+1]
                    ary[i+1] = temp
        k += 1
        j -= 1
    return ary

print 'Bubble Sort:'
ary = [2,5,1,10,20,15,8]
print ary
bubbleSort(ary)
print ary
print ''



def mergeSort(ary):
    if len(ary) == 1 or len(ary) ==0:
        return ary
    else:
        mid = len(ary)/2
        aryA = mergeSort(ary[mid:])
        aryB = mergeSort(ary[:mid])
        return merge(aryA,aryB)


def merge(aryA, aryB):
    aryC = []
    while len(aryA) != 0 and len(aryB) != 0:
        if aryA[0] < aryB[0]:
            aryC.append(aryA[0])
            aryA.pop(0)
        elif aryB[0] < aryA[0]:
            aryC.append(aryB[0])
            aryB.pop(0)
    if len(aryA) == 0:
        aryC += aryB
    else:
        aryC += aryA
    return aryC


print 'Merge Sort:'
ary = [2,5,1,10,20,15,8]
print ary
print mergeSort(ary)
