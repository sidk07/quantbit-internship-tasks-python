# Task 2 
# Read a file containing integers and calculate their sum.

def sumIntegerFile(file) :
    sum = 0
    for i in file :
        sum += int(i)
    return sum
print(sumIntegerFile(open("integerFile.txt")))