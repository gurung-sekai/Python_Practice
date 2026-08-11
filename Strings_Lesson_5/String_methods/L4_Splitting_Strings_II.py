authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Only contains the names of author's names
author_names = authors.split(',')
print(author_names)

# Only containing the last name of author's 
author_last_names = []
for names in author_names:
    author_last_names.append(names.split()[-1])
print(author_last_names)