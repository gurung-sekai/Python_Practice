# You create a dictionary called elements with atomic numbers as keys and element names as values. 
# Then, you remove three elements from elements and store them in a new dictionary reading with custom keys. Finally, you print each key-value pair in reading.

elements = {1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boron", 6: "Carbon", 7: "Nitrogen", 8: "Oxygen", 9: "Fluorine", 10: "Neon", 11: "Sodium", 12: "Magnesium", 13: "Aluminum", 14: "Silicon", 15: "Phosphorus", 16: "Sulfur", 17: "Chlorine", 18: "Argon", 19: "Potassium", 20: "Calcium", 21: "Scandium", 22: "Titanium"}

reading = {}
reading["catalyst"] = elements.pop(6)
reading["core"] = elements.pop(14)
reading["byproduct"] = elements.pop(8)

for key, value in reading.items():
  print("Your " +key+ " element is " + value + ".")

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
  print(element)


inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(inventory.get("stone glove", 30))

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(561721, "No Value")
print(raffle)
