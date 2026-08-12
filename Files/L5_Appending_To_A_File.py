# Add a new line to ‘cool_dogs.txt’ and then print the updated file contents.

with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy\n')

with open('cool_dogs.txt', 'r') as cool_dogs_file:
  print(cool_dogs_file.read())
