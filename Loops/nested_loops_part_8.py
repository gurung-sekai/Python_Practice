# This code loops through each list in sales_data, prints each location’s sales, 
# and adds up all the numbers to calculate the total scoops_sold

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0 

for location in sales_data:
    print(location)
    for element in location: 
        scoops_sold += element

print(scoops_sold)




