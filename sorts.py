
def bubbleSort(ary):
    k = 0
    j = len(ary) - 1
    while k < j:
        print k, j
        for i in range(0,j):
            if i+1 <= j:
                if ary[i] > ary[i+1]:
                    temp = ary[i]
                    ary[i] = ary[i+1]
                    ary[i+1] = temp
        k += 1
        j -= 1
    return ary

ary = [2,5,1,10,20,15,8]
print ary
bubbleSort(ary)
print ary
