# Learning format()

def poem_title_card(title, poet): 
    poet_description = "The poem \"{}\" is written by {}".format(title, poet)
    return poet_description

print(poem_title_card("I Hear America Singing", "Walt Whitman"))