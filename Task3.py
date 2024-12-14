# Task 3 
# Find the second largest number in a list. 

def secondLargNum(lst) :
    mx = lst[0]
    mx2 = lst[1]
    for i in range(2, len(lst)) :
        if(mx < mx2) :
            temp = mx
            mx = mx2
            mx2 = temp
        if(mx2 < lst[i]) :
            mx2 = lst[i]
    if(mx < mx2) :
        temp = mx
        mx = mx2
        mx2 = temp
    return mx2
print(secondLargNum([10, 20, 4, 45, 99]))