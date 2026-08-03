# Some say that every one year of human's life is equivilant to seven years of a dog's life. 
# Write a function named dog_years() that has two parameters named name and age.
# The function should complete the age in dog years and return the following string: 

# "{name}, you are {age} years old in dog years"

def dog_years(name, age): 
    return name+", you are " +str(age * 7) +" years old in dog years."

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# Define function with name and age inputs.
# Return a string with the name and age in dog years (age * 7), converting the number to a string.

