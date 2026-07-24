# Example 1 
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

# Example 2 
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers: 
    if num < 0:
        only_negative_doubled.append(num * 2)

print(only_negative_doubled)
