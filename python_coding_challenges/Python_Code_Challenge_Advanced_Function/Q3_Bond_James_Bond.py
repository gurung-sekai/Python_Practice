# Write a function named introduction() that has two parameters named first_name and last_name 
# The function should return the last_name, followed by a comma, a space, first_name another space, 
# and finally last_name 

def introduction(first_name, last_name):
     return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

# Defined the method to accept the first and last name. 
# On the next line, we performed all the concatenation at once by adding the comma, spaces, and names in the correct order. 
# Returned the same result on the same line. 

