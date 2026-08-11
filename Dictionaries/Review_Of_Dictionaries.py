# How to create a dictionary
# How to add elements to a dictionary
# How to update elements in a dictionary
# How to use a dictionary comprehension to create a dictionary from
# Preview: Docs Used to import specific attributes, classes, or functions from a Python module.two lists

# Create two lists: one for song names and one for play counts
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Use dictionary comprehension and zip to pair each song with its play count
plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)  # Print the plays dictionary

# Add a new song with its play count
plays["Purple Haze"] = 1

# Update the play count for an existing song
plays["Respect"] = 94

# Create a library dictionary with two keys: one for the best songs and one for Sunday Feelings (empty dictionary)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)  # Print the library dictionary

# Important:  Lists cannot be the keys of a dictionary because they are mutable.