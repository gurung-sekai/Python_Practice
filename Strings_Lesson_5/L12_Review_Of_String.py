# Lesson Review:
# - Strings are lists of characters.
# - Access characters with string_name[index], starting at 0.
# - Use slices to get parts of a string.
# - Concatenate strings to make bigger strings.
# - len() gives the number of characters.
# - Use for loops to go through strings.
# - Combining loops and conditionals with strings is powerful.

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[:3]

    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[:4]

    return user_name


def password_generator(user_name):
    password = ""

    for i in range(len(user_name)):
        password += user_name[i - 1]

    return password


user = username_generator("Pritam", "Gurung")

print(user) # Prints PriGuru                  
print(password_generator(user)) # Prints UPriGur

# The code creates a username by combining the first three letters of a first name and the first four letters of a laste name
# (or the whole name if shorter). Then, it creates a password by shifting all the letters of the username to one position on the right 
# moving the last letter to the front. It prints both the username and the password 