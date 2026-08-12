# This code shows how to use a dictionary to store and access related data. 
# Each key (like “earth” or “fire”) maps to a list of zodiac signs. To get the signs for a specific element, use the key in square brackets. 
# This returns the list linked to that key.

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])
