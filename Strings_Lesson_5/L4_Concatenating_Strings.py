# Concatenate essentially means to combine two or more existing strings. 

first_name = "Pritam" 
last_name = "Gurung"

def account_generator(first_name, last_name): 
    account_name = first_name[:3] + last_name[:3]
    return account_name 

new_account = account_generator(first_name, last_name)
print(account_generator("Pritam", "Gurung"))

# or 
# new_account = account_generator(first_name, last_name) 
# print(account_generator)

