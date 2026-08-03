# This project uses Python lists to create and manage a digital gradebook. 
# It stores subjects and grades in a two-dimensional list, adds new classes, updates an existing grade, changes a numerical grade to a Pass/Fail result, and combines gradebooks 
# from two semesters into one complete record.



last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Checkpoint 1 
subjects = ["physics", "calculus", "poetry", "history"]
grades = ["98", "97", "85", "88"]
subjects.append("computer science")

# Checkpoint 2
gradebook = [["physics", 98], 
["calculus", 97], 
["poetry", 85], 
["history", 88]
]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[2].remove(85)
gradebook[2].append("Pass")
gradebook[-1][-1] += 5


# Checkpoint 3 
full_gradebook = last_semester_gradebook + gradebook 

print(full_gradebook)

