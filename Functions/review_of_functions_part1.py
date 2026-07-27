#Code Below 
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Pritam")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.6)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Honolulu", "Hilo",  estimate, "plane")

# Functions organise code into reusable blocks.

# Without functions, code becomes repetitive and harder to maintain.

# A function is defined using the `def` keyword.
# Indentation separates the code inside a function from code outside it.

# Parameters are variables listed in a function definition.
# Arguments are the actual values passed into a function.

# Built-in functions, such as print() and len(), are provided by Python.
# User-defined functions are functions created by the programmer.

# The `return` keyword sends a result back to where the function was called.
# A function can also return multiple values.

# Variable scope determines where a variable can be accessed.
# Local variables are usually available only inside their function.

# These concepts allow programs to be more reusable, organised, and readable.