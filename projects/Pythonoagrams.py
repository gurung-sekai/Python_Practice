# Pythonagrams
# Your friends are playing Pythonagrams and need a better way to keep score! 
# Use Python dictionaries to build a scoring system that tracks players, words, and points.
# In Pythonagrams, each letter is worth a given number of points, and words are scored based on the sum of the values of the letters.
# There are many ways you can extend this project on your own if you finish and want to get more practice!
# If you get stuck during this project or would like to see an experienced developer work through it, select “Get Unstuck” to see a project walkthrough video.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

# Task 1
letter_to_points = {
    letter: point for letter, point in zip(letters, points)
}


# Task 2
# print(letter_to_points)


# Task 3
def score_word(word):

    # Task 4
    point_total = 0

    # Task 5
    for letter in word:
        point_total += letter_to_points.get(letter, 0)

    # Task 6
    return point_total


# Task 7
brownie_points = score_word("BROWNIE")


# Task 8
print(brownie_points)


# Task 9
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}


# Task 10
player_to_points = {}


# Task 11
for player, words in player_to_words.items():
    player_points = 0

    # Task 12
    for word in words:
        player_points += score_word(word)

    # Task 13
    player_to_points[player] = player_points


# Task 14
print(player_to_points)




