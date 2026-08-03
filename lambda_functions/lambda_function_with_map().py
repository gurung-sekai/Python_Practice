# The map() function applies the given lambda function to each item in a list:

numbers = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Prints: [1, 4, 9, 16, 25] 
