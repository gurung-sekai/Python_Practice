current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense 

shirt_expense = 9 

new_budget_after_shirt = deduct_expense( current_budget, shirt_expense )
print_remaining_budget(new_budget_after_shirt)


# This code starts with a budget of $3500.75, prints it, subtracts the $9 shirt expense using deduct_expense(), stores the new budget, and then prints the remaining amount: $3491.75.
