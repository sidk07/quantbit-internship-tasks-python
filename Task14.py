# Task 14 
# Count word frequency in a paragraph.

def countWordes(str) :
    lst = str.split()
    dict = {}
    for word in lst :
        if word in dict :
            dict[word] += 1
        else :
            dict[word] = 1
    for k, v in dict.items() :
        print(k,":",v)
        
countWordes("apple banana apple orange banana banana" )

