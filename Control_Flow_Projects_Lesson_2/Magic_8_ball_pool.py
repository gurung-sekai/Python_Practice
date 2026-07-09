### Project Focusing on Control Flow using if/elif/else statement for this project 

import random

# Setting up the answer

name = "Max"
question = "Will England win the World Cup?"
answer = ""

# Generating a random number 

random_number = random.randint(1, 9)

# If statements 

if random_number == 1: 
  answer = "Yes - definitely"
elif random_number == 2: 
  answer = "It is decidedly so"
elif random_number == 3: 
  answer = "Without a doubt"
elif random_number == 4: 
  answer = "Reply hazy, try again"
elif random_number == 5: 
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7: 
  answer = "My sources say no"
elif random_number == 8: 
  answer = "Outlook not so good"
elif random_number == 9: 
  answer = "Very doubtful"
else: 
  print("Error")

print(name + " asks: " + question)
print("Magic 8 Ball's answer: " + answer)







