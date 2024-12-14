# Task 5 
# Validate user input as an integer.

def validateInput() :
    while True :
        value = input("Enter value : ")
        if(not value.isdigit()) :
            print("Invalid input. Please enter a number.")
        else : 
            break
    print("You entered: ", value)
validateInput()