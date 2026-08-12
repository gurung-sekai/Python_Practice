# You used the .values() method to access all the values in a dictionary. Then, you looped through these values to calculate a running total. 
# This shows how to work with dictionary values for tasks like summing numbers.

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0 
for exercises in num_exercises.values():
  total_exercises += exercises
  print(total_exercises)
