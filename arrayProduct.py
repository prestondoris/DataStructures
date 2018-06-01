# coding: utf-8

def array_of_array_products(arr):
# Given an array of integers arr, you’re asked to calculate for each index i
# the product of all integers except the integer at that index
# (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an
# array of integers and returns an array of the products.
#
# Solve without using division and analyze your solution’s time and space complexities.

    if len(arr) == 0 or len(arr) == 1:
        return []
#  i = 0
#  j = 1
#  value = 1
#  while i < len(arr):
#    while j < len(arr):
#      if j != i:
#        value *= arr[j]
#      j += 1
#    ans.append(value)
#    j = 0
#    i += 1
#    value = 1
#  return ans
    print arr

    left =[1]
    right = [1]
    for i in range(len(arr)-1):
        left.append(left[-1]*arr[i])
        print left
    print left
    print ''

    for j in range(len(arr)-1,0,-1):
        right.append(right[-1]*arr[j])
        print right
    right.reverse()
    print right
    print ''

    for k in range(len(arr)):
        arr[k] =  left[k] * right[k]

    return arr




arr = [8, 10, 2]
print array_of_array_products(arr)
print ''
print ''
arr = [8, 10, 2, 15, 3]
print array_of_array_products(arr)
