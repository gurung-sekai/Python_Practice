# Write a function named combine_sort() that has two parameters named my_list1 and my_list2.
# The function should combine these two list into one new list and sort the result. 
# Return the new sorted list. 

def combine_sort(my_list1, my_list2): 
    unsorted_list = my_list1 + my_list2
    sorted_list = sorted(unsorted_list)
    return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# We start by combining the two lists together using + in order to get a new list.
# Next, to sort them, we use the sorted() function which returns a new sorted version of the list.