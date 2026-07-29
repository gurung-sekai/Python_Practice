# Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name): 
    if (your_name == my_name): 
        return True
    else: 
        return False

print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))

# As you can see in this solution code, comparing two strings in python can be done using the == operator. 
# If you want an added challenge, you can try shortening the function body to one line of code!

def same_name(your_name, my_name):
    return your_name == my_name


print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))


