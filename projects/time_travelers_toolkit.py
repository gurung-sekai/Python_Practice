# Task 3
# Create the main script: time_travelers_toolkit.py


# Task 4
# Import the necessary modules

import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module


# Task 5
# Get today's date and current time

today = dt.date.today()
current_time = dt.datetime.now().time()


# Task 6
# Print the current date and time

print(f"Today's date is: {today}")
print(f"The current time is: {current_time}")


# Task 9
# Generate a random year

random_year = randint(1900, 2100)


# Task 10
# Create a list of destinations
# Randomly select one destination

destinations = [
    "Paris",
    "Tokyo",
    "New York",
    "Ancient Rome",
    "London"
]

destination = choice(destinations)


# Task 7
# Calculate the cost of time travel using Decimal

base_cost = Decimal("1000.00")

year_difference = abs(today.year - random_year)

cost_multiplier = Decimal(str(year_difference))

final_cost = base_cost + cost_multiplier


# Task 8
# Format the final cost to two decimal places

formatted_cost = f"{final_cost:.2f}"


# Task 11
# Generate the time travel message using our custom module

message = custom_module.generate_time_travel_message(
    random_year,
    destination,
    formatted_cost
)

print(message)