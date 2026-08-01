# Create a function named larger_sum() that takes two list of numbers as paramters named 1st and 1st2
# The funcion should return the list whose elements sum to the greater number. If the sum of 
# the elements of each list are equal, return 1st1. 

def larger_sum(lst1, lst2): 
    sum_1 = 0 
    sum_2 = 0
    for numbers in lst1: 
        sum_1 += numbers
    for numbers in lst2: 
        sum_2 += numbers
    if (sum_1 >= sum_2):
        return lst1
    else: 
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

# Ths solution, it manually iterates through each element in each list and calculates the sum. 
# We then return the list with greater sum and break the tie by returning the lst1. 