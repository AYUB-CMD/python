#wap to display a user entered naem followed by good morning using input function

greeting = "Good morning,"
#name = input("enter your name")

#print (greeting+name)


#wap to fill in a letter template given below



letter = '''Dear <|name|> \n You\'re selected1 \n <|date|>'''
#name = input("enter ur name")
#date = input("enter ur date")
#letter =letter.replace("<|name|>", name)
#letter =letter.replace("<|date|>",date)
#print(letter) 


#wap to detect double quotes in a string
sentence = "this is string with double  spaces"

doubleSpaces = sentence.find("  ")
#print(doubleSpaces)


#wap to replace double quotes form problem 3 with single quote

sentence = "this is string with double  spaces"
doubleSpaces = sentence.find("  ")
singleSpace = sentence.replace("  ", " ")
print(singleSpace)

#wap to formate the following letter using escape sequence character

letter = "dear marry! \n this python course is nice \n thank\'s"

#print(letter)
