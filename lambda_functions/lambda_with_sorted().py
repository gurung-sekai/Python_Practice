# The sorted() function can use a lambda function as a key for custom sorting: 

students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
sorted_students = sorted(students, key=lambda x: x[2]) 

print(sorted_students) 
# Prints: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 

# In this case, the lambda function lambda x: x[2] is used as the key for sorting. 
# It tells the sorted() function to use the third element (index 2) of each tuple for comparison.
#  As a result, the list of students is sorted by age (the third element in each tuple).