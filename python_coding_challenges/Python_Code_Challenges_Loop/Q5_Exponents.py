# Create a function named exponents() that takes two lists as parameters named bases and powers.
# Return a new list containing every number in bases raised to every number in powers.
# For example, consider the following code.

# exponents([2, 3, 4], [1, 2, 3])

# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. 
# It would first add two to the first. Then two to the second. Then two to the third, and so on.

def exponents(bases, powers): 
    new_list = []
    for base in bases: 
        for power in powers: 
            new_list.append(base ** power)
    return new_list

print(exponents([2, 3, 4], [1, 2, 3]))

#As you can see in this solution, we used two nested for loops so that, for every base, we iterate through every power. 
# This allows us to raise each base to every single power in our list and append the answers to our new list. 
# Finally, we return the list of answers.
