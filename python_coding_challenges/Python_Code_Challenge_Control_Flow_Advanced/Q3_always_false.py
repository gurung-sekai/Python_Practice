# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.
# An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

def always_false(num):
    if (num > 0 and num < 0): 
        return True
    else: 
        return False 

print(always_false(-1))
print(always_false(0))
print(always_false(1))

# In our example, we use the contradiction of being greater than and less than 0 at the same time.
# No matter what value we pass into the function, our condition will always be false since it is not logically possible. You normally want to avoid creating conditions like this.
