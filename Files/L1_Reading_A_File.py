# You’re using a with statement to open welcome.txt safely. 
# Inside, you read the file’s contents into text_data, then print it. This ensures the file closes automatically when you’re done.

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data) 