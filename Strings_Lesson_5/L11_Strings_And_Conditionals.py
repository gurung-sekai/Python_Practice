def contains(big_strings, little_strings):
    return little_strings in big_strings

def common_letters(string_one, string_two): 
    common = [] 
    for letters in string_one: 
        if (letters in string_two) and not (letters in common): 
            common.append(letters)
    return common

print(common_letters("banana", "cream"))

# Prints the common letter between two words 