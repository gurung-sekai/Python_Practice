# The basic syntax of Lambda Function 
# lambda [parameter] : [expression]

# Lambda function to add two numbers 
add = lambda a, b: a + b 

print(add(3, 5)) # Prints 8 

# Lambda function to print a name 
greetings = lambda name: "Hello, " + name + "!"
print(greetings("Pritam")) # Prints: Hello, Pritam!
