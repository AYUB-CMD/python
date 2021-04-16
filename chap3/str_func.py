story = "once  upon a time there was a ninja whose name is Naruto, he has kurama in his belly locked inside"

print(story[0:4])

#string function

print(len(story))  #return length os strings
print(story.endswith("side"))
print(story.count("n"))
print(story.capitalize())
print(story.find("ninja"))
print(story.replace('kurama', 'jinjuriki'))


#escape sequence character

line = "once  upon a time \n there was a ninja whose name is Naruto,\t he has kurama in his belly\'s locked inside"
print(line)

'''\n new line
\t tab
\' single qoute
\\ backslash'''