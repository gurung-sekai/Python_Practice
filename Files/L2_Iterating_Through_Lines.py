# You are opening the file how_many_lines.txt and reading each line one by one using a for loop. 
# For every line, you print its contents to the screen. This is a great way to display a file’s lines

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines(): 
    print(line)