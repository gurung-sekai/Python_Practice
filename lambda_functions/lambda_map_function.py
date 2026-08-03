# The basic syntax of map() 
# map(function, iterable, [iterable2, iterable3, ...]) 


# How map() works 

def double(x): 
    return x * 2 

numbers = [1, 2, 3, 4, 5] 
doubled_numbers = map(double, numbers) 

print(list(doubled_numbers))  # Prints: [2, 4, 6, 8, 10] 

# In this example, map() applies the double function to each number in the numbers list, 
# creating a new iterator with the results.

# Converting strings to integers 
str_nums = ['1', '2', '3', '4', '5'] 
int_nums = list(map(int, str_nums))

print(int_nums)  # Prints: [1, 2, 3, 4, 5] 

# Finding the length of strings 
words = ['apple', 'banana', 'cherry'] 
word_lengths = list(map(len, words)) 

print(word_lengths)  # Prints: [5, 6, 6] 

# Using map() with Lambda function 
numbers = [1, 2, 3, 4, 5] 
doubled = list(map(lambda x: x * 2, numbers)) 

print(doubled)  # Prints: [2, 4, 6, 8, 10] 

# Multiple iterables with map()
list1 = [1, 2, 3] 
list2 = [10, 20, 30] 

result = list(map(lambda x, y: x + y, list1, list2)) 

print(result)  # Prints: [11, 22, 33] 