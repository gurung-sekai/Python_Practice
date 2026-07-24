# This code takes a list of grades and creates 
# a new list where each grade is increased by 10 points. 
# It then prints the updated list of grades.


# Example 1
grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [num + 10 for num in grades]
print(scaled_grades)

# Example 2 
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers: 
    doubled.append(number * 2)

print(doubled)

# Another example 
desired_list = [-1, 0, 1, 2, 3]
list = [i-1 for i in range(5)]
print(list)

# The loop prints 1 twice, and when it reaches 2 (an even number), 
# 2 % 2 == 0 is True, so break exits the loop before printing 2.

numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

# When the loop reaches element 2, it skips to the next iteration printing 3 
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    continue
  print(number)

# Prints 5 three times. 
for i in range(3):
  print(5)