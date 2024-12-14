# Task 1 
# Reverse a string without using built-in methods. 

def revString(str) :
    revStr = ""
    for i in str :
        revStr = i + revStr
    return revStr
print(revString(str = input("Enter String : ")))
