 # Dictionary comprehension is a way to quickly create dictionaries from pairs of data. 
 # The lesson shows how to use a special syntax: {key: value for key, value in iterator}.
 # In the code, zip(drinks, caffeine) creates pairs, and the comprehension turns each pair into a key-value entry in the new dictionary. 
 # This method is efficient for building dictionaries from two related lists.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}

print(drinks_to_caffeine)