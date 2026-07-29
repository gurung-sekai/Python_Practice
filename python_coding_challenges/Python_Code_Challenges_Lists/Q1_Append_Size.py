# Create a function called append_size() that has one parameter named my_list.
# The function should append the size of my_list (inclusive) to the end of my_list. 

# The function should then return this new list.
# For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

def append_size(my_list):
  length = len(my_list)
  my_list.append(length)
  return my_list

print(append_size([23, 42, 108]))

# Alternative 

def append_size(input_list):
  input_list.append(len(input_list))
  return input_list

print(append_size([23, 42, 108]))