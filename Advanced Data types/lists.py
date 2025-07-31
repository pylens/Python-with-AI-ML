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


# removing elements from list
# 1. remove() : it will remove the first occurrence of the element
print(items)
items.remove('delta')
print(f"items after removing using remove : {items}")

# 2. pop(): it will remove the element at specific index position
items.pop()
print(f"items after removing using pop: {items}")
items.append('100')
# 3. del: it will remove the element at specific index position
del items[2]
print(f"items after removing using del: {items}")

# del items
# print(items)

# items.clear()
# print(items)

# sort: it will sort the list in ascending order or descending

items.sort(reverse=True)

print(f"after sorting: {items}")

# adding or joining two or more lists

items2 = [2,4,5,6]

# direct concatination
# itemsRes=items + items2
# print(itemsRes)

# extends()
items.extend(items2)
print(items)
print(items2)

items.reverse()
print(items)