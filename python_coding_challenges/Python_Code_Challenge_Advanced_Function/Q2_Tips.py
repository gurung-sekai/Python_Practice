# Create a function called tip() that has two parameters named total and percentage. 
# The function should return the amount you should tip given a total and the percentage you want to tip. 

def tip(total, percentage): 
    tip_amount = (total * percentage) / 100
    return tip_amount

print(tip(10, 25)) # Prints 2.5
print(tip(0, 100)) # Prints 0 

# Define function with two inputs.
# Multiply total by percentage and divide by 100.
# Return the tip amount.
