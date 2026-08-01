# Create a function named max_num() that takes a list of numbers named nums as a paramter 
# The function should return the largest numbers in nums 

def max_num(nums): 
    maximum = nums[0]
    for numbers in nums: 
        if (numbers > maximum): 
            maximum = numbers
    return maximum 

print(max_num([50, -10, 0, 75, 20]))

# There are a few different ways to accomplish the task, but the way we did it was to check every element
# in the lust and see if there is one bigger than what we currently think is the biggest. If there is a bigger one 
# then replace it. We keep replacing the number until the largest number has been found. 

