inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Checkpoint 1 & 2
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory.sort()

# Print
print(inventory_len)
print(first)
print(last)
print(inventory_2_6)
print(first_3)
print(twin_beds)
print(removed_item)
print(inventory)
