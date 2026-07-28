# Use map() with a lambda function to create a new list called tripled that contains each number multiplied by 3 and print tripled.
# Then, use filter() with a lambda function to create a new list called greater_than_15 
# that contains only the values from numbers that are greater than 15 and print greater_than_15.

numbers = [5, 12, 17, 24, 30, 7, 18]

# map() function 
tripled = list(map(lambda x : x * 3, numbers))
print(tripled)

# filter() function 
greater_than_15 = list(filter(lambda x : x > 15, numbers))
print(greater_than_15)
