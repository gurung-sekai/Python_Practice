# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. 
# Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num): 
    if (num % 10 == 0): 
        return True 
    else: 
        return False 

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# In this solution, we perform the modulus operation within the condition of the if statement.
#  We test if the result is equal to 0 and if it is, then we return True otherwise we return False.