# String methods learned in this lesson:
# .upper() - returns a copy of the string with all letters uppercase.
# .title() - returns a copy of the string with each word capitalized.
# .lower() - returns a copy of the string with all letters lowercase.
# .split() - splits a string into a list of substrings.
# .join() - joins a list of strings into a single string.
# .strip() - removes whitespace or specified characters from the start and end.
# .replace() - replaces all instances of a substring with another substring.
# .find() - returns the index of the first occurrence of a substring.
# .format() - inserts variables into a string using placeholders.


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

highlighted_poems_stripped = [] 
for poems in highlighted_poems_list: 
  highlighted_poems_stripped.append(poems.strip())

highlighted_poems_details = []
for poem in highlighted_poems_stripped: 
  highlighted_poems_details.append(poem.split(':'))

titles = [] 
poets = [] 
dates = []

for poem in highlighted_poems_details: 
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

for i in range(0,len(highlighted_poems_details)): 
  print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
  
print(highlighted_poems_stripped)