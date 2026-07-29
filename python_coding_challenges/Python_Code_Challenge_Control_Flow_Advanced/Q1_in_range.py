# Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
    if (num >= lower and num <= upper): 
        return True
    else: 
        return False 

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))

# In this solution, we test the two bounds connected with an and boolean operator. 
# This means that the code nested in the if statement will only execute if both of the conditions are true. 
# We also do not include the else statement here. 
# Since our if statement will return True and exit the function if the condition is true, the last line will only be reached if the condition was false.