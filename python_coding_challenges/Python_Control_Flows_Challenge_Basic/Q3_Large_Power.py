# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent): 
    if base ** exponent > 5000: 
        return True 
    else: 
        return False 

print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# In this solution, we have an example of how the operation can be performed in the condition of the if statement. This prevents us from needing to create an extra variable. 
# If the condition is true, then the indented code is executed which returns True, otherwise the indented code in the else statement is executed.

