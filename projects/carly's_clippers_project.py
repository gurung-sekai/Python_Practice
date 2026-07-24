# Use your newfound knowledge of loops to discover trends in the operation of the newest hair salon in town, Carly’s Clippers.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Prices and cuts 
total_price = 0 
for price in prices: 
    total_price += price

average_price = total_price / len(prices)
print("Average Price:", str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

# Revenue
total_revenue = 0 
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue:", str(total_revenue))

# Average revenue 
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] 
                 for i in range(len(hairstyles)) 
                 if new_prices[i] < 30]

print(cuts_under_30)

