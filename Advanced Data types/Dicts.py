phonebook = {
    "Alice": "555-1234", #('alice', '555-1234'), ("Bob", "555-5678")
    "Bob": "555-5678",
    "Charlie": "555-9999",
    (1,2): {'one':'two'},
    "Diana": {'adderess': "california", 'pincode': 50081} # key-value pair
}
print(phonebook)

print(phonebook['Alice'])
print(f"keys of the dict is : {phonebook.keys()}")
print(f"values of the dict is : {phonebook.values()}")
print(f"items of the dict is: {phonebook.items()}")
print(f"the tyoe oif dict_items is : {type(phonebook.items())}")

dict_items = phonebook.items()
tem=list(dict_items)
print(f"after conversion of dict_items we have : {tem} and the data type of it is {type(tem)}")
print(f"the first item of dict_items is : {tem[0]} and the type of it is {type(tem[0])}")

# access value of a dict using key
print("*"*30)
print(f"{phonebook[(1,2)]} and the data type is {type(phonebook[(1,2)])}")

# option 1
print(phonebook['Diana']['adderess'])
#option 2
dianaDetails = phonebook['Diana']
print(dianaDetails['adderess'])
print(f"diana details are : {dianaDetails}")


# method two for creating a dicgt

dict2=dict(
    Alice = "555-1234", 
    Bob = "555-5678",
    Charlie= "555-9999",
)
print(dict2)

# mthod 3
pairs = [("name", "John"), ("age", 25)]
print(f"{pairs} and the type is {type(pairs)}")
user = dict(pairs)
print(user)



print(phonebook.get('Alice', "Key not found"))

phonebook['email'] = {'personal':'alice@gmail.com', "bussiness" : 'bob@gmail.com'}
print(phonebook)


print(phonebook.pop("email", 'Key not found'))
print(phonebook)
