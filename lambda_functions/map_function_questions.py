# Use map() to convert the strings in str_numbers to integers and store the result in a list called convert_int, and print convert_int.
# Then, use map() with a lambda function to add corresponding elements from list_a and list_b and store the result in a list called convert_sum, and print convert_sum. 
# Index 0 of convert_sum should be the sum of the elements at index 0 from both list_a and list_b, and so on.
# Finally, use a list comprehension (as an alternative to map) to square each number in numbers, store the results in a list called convert_square, and print convert_square.

str_numbers = ["10", "20", "30", "40", "50"]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
numbers = [2, 4, 6, 8, 10]

# write your code below
# Convert the strings to integers 
convert_int = list(map(int, str_numbers))
print(convert_int)

# With a lambda function to add corresponding elements
convert_sum = list(map(lambda x, y: x + y, list_a, list_b))
print(convert_sum)

# A list comprehension
convert_square = [x ** 2 for x in numbers]
print(convert_square)
