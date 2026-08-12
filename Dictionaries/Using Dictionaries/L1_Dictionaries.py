# This code creates a dictionary named student with keys for name and age.
# Then, it adds grade and subject to the dictionary using the .update() method. Finally, it prints the dictionary before and after updating.

# Checkpoint 1: Create the initial dictionary
student = {
  'name': "Alice", 
  "age": 21}
print(student)


# Checkpoint 2: Add more details using update()
student.update({
  "grade": 'A', 
  "subject": 'Math'})
print(student)