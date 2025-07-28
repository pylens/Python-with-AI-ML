# list is one of the data type which can store n number items in it and those items can be different data types like int, str, float, bool or even another list.
# 1. ordered : it has some fixed order 
# 2. changeable : it can be changed after it is created
# 3. indexed: it can be accessed by index starts from 0 to number elements
# 4. Allow duplicates: duplicate elements can be accecepted

items = ['hemanth', 'hyderabad', 70000, 'hemanth', 'apple'] # -4 -3 -2 -1 0 1 2 3 4...
# items.append('ML Engineer')
# index: it is the position of the element and it starts with zero
print(items)

print(f"the first element in the list is: {items[0]}")
print(len(items))

# items.pop(2)
print(f"after deletion elemetns are : {items}")

# print(items[6])

# list constructor is written as list()
clist = list(("harish", "elecrtical engineer", 80000))
print(clist)


# access list elements
print(items[0:3]) # in index range the last element is excluded
# print(items[4])
print(items[-3:-1])

# membbership operators

print("h" in items)
# identity operator
print(clist is clist)

# isnert itelm at spesific postion
print(f"before isnerting: {items}")
items[2:4] = "alpha", "beta", "captain", "delta"
print(f"after inserting: {items}")

# insert() : it will insert an element at specific index postion

print(f"{clist}")
clist.insert(2, "0")
print(clist)



