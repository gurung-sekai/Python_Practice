# Write a function named larger_list() that has two parameters named my_list1 and my_list2.
# The function should return the last element of the list that contains more elements. 
# If both lists are the same size, then return the last element of my_list1.

def larger_list(my_list1, my_list2): 
    if len(my_list1) >= len(my_list2): 
        return my_list1[-1]
    else: 
        return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10])) # Should print 5 

# We start by comparing the lengths of each of the lists using the len() function. 
# This determines whether to return the last element of the first list or the second list. Notice that we use >=. 
# This way, we know what to do if the lists have an equal length.
# In order to get the last element, we get the element at the -1 index.
# The negative index starts at the end of the list and works towards the start of the list.