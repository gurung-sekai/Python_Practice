# This code adds a new key-value pair to the dictionary.
# It then checks if the key exists before printing its value. This helps avoid errors when accessing keys that might not be in the dictionary.

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements: 
  print(zodiac_elements["energy"])
