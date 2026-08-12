# You’re creating two dictionaries: user_ids for usernames and IDs, and num_exercises for lesson names and exercise counts. 
# Then, you get all the keys from each dictionary using .keys() and print them with print(users) and print(lessons).

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)