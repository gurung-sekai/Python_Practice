# Create a function called max_num() that has three parameters named num1, num2, and num3.
# The function should return the largest of these three numbers. 
# If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1, num2, num3): 
    if (num1 > num2 and num1 > num3): 
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    elif (num3 > num1 and num3 > num2):
        return num3
    else: 
        return("It's a tie!")

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

# In this code, we use a series of if, elif, and else statements.
# We test the first parameter against the other two parameters and return the value if it is greater than the other two.
# We have two more tests to check if the second parameter is greater than the other two, then if the third parameter is greater than the other two. In the case where none of the parameters were greater than both of the other parameters, 
# then we know that there must have been a tie and the final return statement is reached.