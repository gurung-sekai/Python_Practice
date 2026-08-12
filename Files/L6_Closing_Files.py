# Open 'fun_file.txt' and assign the file object to close_this_file
with open('fun_file.txt') as close_this_file:

  # Read the first line from the file
  setup = close_this_file.readline()
  # Read the second line from the file
  punchline = close_this_file.readline()

  # Print the first line
  print(setup)
