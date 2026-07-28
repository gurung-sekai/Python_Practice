# Using Lambda with filter() 

# The filter() function creates a new list of elements which the given lambda function returns True:
# The filter() function uses this lamba to keep only the even numbers from the original list 
# lambda x: x % 2 == 0 checks if a number is even  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Prints [2, 4, 6, 8, 10]