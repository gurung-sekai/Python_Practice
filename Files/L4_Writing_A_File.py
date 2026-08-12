 # You are opening the file bad_bands.txt for writing using a with statement, writing Lepauch to it, and then printing the file object bad_bands_doc after the file is closed.


with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('Lepauch') 

print(bad_bands_doc)