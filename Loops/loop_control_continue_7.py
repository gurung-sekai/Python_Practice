# Without the continue statement, 
# the code would print every age in the list, including those under 21.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
    if i < 21: 
        continue 
    print(i)
