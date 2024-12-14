# Task 13 
# Implement the binary search algorithm.

def binarySearch(lst, target) :
    lst.sort()
    low = 0
    high = len(lst) - 1
    while True :
        mid = (low + high) // 2
        if target == lst[mid] :
            break
        elif target < mid :
            high = mid
        else :
            low = mid
    return mid
print("Found at index : ", binarySearch([1, 3, 5, 7, 9], 7))