#dictionary
# collection of key value pairs

my_Dictionary = {
    "name": "ayub",
    "ocupation": "software engineer",
    "marks": [98, 97, 97],
    "another dictionary": {
        "name": "naruto",
    "ocupation": "ninja",
    }
}

print(my_Dictionary["name"])
print(my_Dictionary["marks"])
print(my_Dictionary["another dictionary"]["name"])

#changing value which is mutable
my_Dictionary["marks"] = [00, 9, 98]
print(my_Dictionary["marks"])