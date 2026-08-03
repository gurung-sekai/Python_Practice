first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
print("My name is " + fixed_first_name + " " + last_name)
print(f"My name is {fixed_first_name} {last_name}")

# Strings are immutable which means you cannot change a string after it is created. 
# Hence you must make a new string and the original string remains the same. 