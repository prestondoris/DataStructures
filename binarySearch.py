
def binarySearch(ary, val):
    # ary must be a sorted before calling this function
    low = 0
    high = len(ary)-1
    while low <= high
        mid = (high + low)/2
        if val == ary[mid]:
            return mid
        elif val > ary[mid]:
            low = mid + 1
        elif val < ary[mid]:
            high = mid - 1
    return False
