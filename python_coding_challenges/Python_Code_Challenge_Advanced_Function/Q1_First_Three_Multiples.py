# Write a function named first_three_multiples() that has one paramter named num
# The function should print the first three multiples of the num. Then, it should return the third multiple. 
# For example, first_three_multiple(7) should print 7,14 and 21 on three different lines, and return 21. 

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

first_three_multiples(10) # Should print 10, 20, 30, and return 30 
first_three_multiples(0) # should return 0, 0, 0 and return 0 

# Define function with one input.
# Print input times 1, 2, and 3.
# Return input times 3.
