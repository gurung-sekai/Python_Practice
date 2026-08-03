def letter_check(word, letter):
    for charector in word: 
        if charector == letter: 
            return True
         
    return False

print(letter_check("Strawberry", "a"))
print(letter_check("Strawberry", "o"))

# return False must be outside of the loop to ensure that it does not return False immeidiately after 
# checking the letters. 