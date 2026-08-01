# Write a function named same_values() that takes two list of numbers of equal size as parameters. 
# The function should return a list of the indicies where  the values were equal in lst1 and lst2. 
# For example, the following code should return [0, 2, 3]

# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

def same_values(lst1, lst2): 
    new_lst = [] 
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append(index)
    return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# In this solution, we used a loop that iterates using the range of the len out of our list. 
# This generates the indicies we need to  iterate through. 
# Now that we assume the list are of equal size. We then access the elements at the current index 
# from each list using lst1[index] and lst2[index]. If they are equal we add the index to the new list. 
# Finally, we return the result.