# Create a function named lots_of_math(). This function should have four parameters named a,b,c and d. 
# The function should print 3 lines and return 1 value. 

# First print the sum of a and b 
# Second, print c minus d
# Third, print the first number printed, multiplied by the second number printed. 

def lots_of_math(a, b, c, d): 
    first = a + b 
    second = c - d
    third = first * second 
    fourth = third % a 
    print(first)
    print(second)
    print(third)
    return fourth 


print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

# After defining the function, we store each result into its own variable for first and second 
# We then use these two variables in the calculation for third and we use the value of the third to get fourth. 
# Afterwards, we print the first three variables and return the fourth one. 