# You’re creating a dictionary called pct_women_in_occupation to store job titles and the percentage of women in each. 
# Then, you loop through each item and print a message showing the percentage of women in each occupation.

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items(): 
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.")