# How to write a loop 
# How to use range in a loop 
# How to write a while loop 
# What infinite loops are and how to avoid them 
# How to control loops using break and continue 
# How to write elegant loops as list comprehensions 

single_digits = range(10)
squares = [] 

for element in single_digits: 
    print(element)
    squares.append(element**2)

print(squares)

cubes = [element**3 for element in single_digits]
print(cubes)

desired_list = []
for i in range(5):
    desired_list.append(i - 1)
print(i)