# SUMMARY OF THE CODE

# 1. Read passwords.csv and collect all compromised usernames.

# 2. Save the compromised usernames into compromised_users.txt.

# 3. Create boss_message.json to report that the mission was successful.

# 4. Overwrite passwords.csv with Slash Null's signature.

# Task 1: Import the csv module
import csv


# Task 2: Create a list to store the compromised users
compromised_users = []


# Task 3: Open passwords.csv and save the file object as password_file
with open("passwords.csv", "r") as password_file:

  # Task 4: 
  password_csv = csv.DictReader(password_file)
  
  # Task 5:
  for password_row in password_csv:

    # Task 6: Print each compromised username
        # NOTE: This is removed in Task 7
        # print(password_row["Username"])

        # Task 7
        compromised_users.append(password_row["Username"])
  
# Task 8
with open('compromised_users.txt', 'w') as compromised_user_file: 
  # Task 9
  for compromised_user in compromised_users: 
    # Task 10 
    compromised_user_file.write(compromised_user + "\n")

# Task 11 Complete 


# Task 12
import json 

# Task 13 
with open('boss_message.json', 'w') as boss_message:
  # Task 14 
  boss_message_dict = {
    "reciept": "The Boss", 
    "message": "Mission Success"
  } 

  # Task 15
  json.dump(boss_message_dict, boss_message)

# Task 16
with open('password.csv', "w") as new_passwords_obj: 
    # Task 17
    slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
    # Task 18: Write the signature to passwords.csv
    new_passwords_obj.write(slash_null_sig)



  








