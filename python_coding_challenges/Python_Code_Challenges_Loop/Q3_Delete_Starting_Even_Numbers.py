# Write a function called delete_starting_events() that has a parameter named my_list. 
# The function should remove elements from the front of my_list until the front of the list is not even. 
# The function should then return my_list.
# For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even. 

def delete_starting_evens(my_list):
    while(len(my_list) > 0 and my_list[0] % 2 == 0): 
        my_list = my_list[1:]
    return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
    
# After defining our method, we use a while loop to keep iteratinf as long as some provided conditions are true. 
# We provide two conditions for the while loop to continue. 
# We will keep iterating as long as there is at least one number left in the list len(my_list) > 0 and if the 
# first element in the list is even my_list[0] % 2 == 0. If both of these conditions are true, then we replace
# the list with every element except for the first one using my_list[1:]. 
# Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list. 