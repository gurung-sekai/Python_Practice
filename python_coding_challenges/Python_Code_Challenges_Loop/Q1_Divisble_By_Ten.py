# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter. 
# Return the count of how many numbers in the list are divisible by 10. 

def divisible_by_ten(nums):
    counter = 0 
    for numbers in nums: 
        if (numbers % 10 == 0): 
            counter += 1
    return counter 

print(divisible_by_ten([20, 25, 30, 35, 40]))

# We defined the function and set up our counter. 
# We use a for loop to iterate through each number and check if it is divisible by 10. 
# If a number is divisible by another number than the remainder should be zero, so we use modulus. 
# After the loop has finished, we return our count. 