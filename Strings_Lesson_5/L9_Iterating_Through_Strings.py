# Iterating through Strings 

def get_length(string): 
    counter = 0 
    for length in string: 
        counter += 1 
    return counter 

print(get_length("Pritam"))

# This function counts how many characters are in a string by going through each character one by one and adding to a counter. 
# It returns the total number of characters.