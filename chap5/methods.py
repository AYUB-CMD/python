#methods of dictionary

my_Dictionary = {
    "name": "ayub",
    "ocupation": "software engineer",
    "marks": [98, 97, 97],
    "another dictionary": {
        "name": "naruto",
    "ocupation": "ninja",
    }
}


# dictionarymethods
print(my_Dictionary.keys())  #prints keys of dictionary
print(list(my_Dictionary.keys()))  #converting to list
print(my_Dictionary.values())  #prints values of dictionary
print(my_Dictionary.items())  # returns a list of (key and values) tuples which can be iterate
print(my_Dictionary)
ayub = {
    "lol":"laugh out loud"
}
my_Dictionary.update(ayub) #update the dictionary with supplied key values pairs
print(my_Dictionary)


#both are not same get return none doesnt throw error but [ this does]
print(my_Dictionary.get("name"))# returns none when there is  not present 
print(my_Dictionary["name"]) # throws error when there is  not present 