my_tuple = (1, 2, "apple", (3, 4), "apple") # nested tuple
print(f" tuple is {my_tuple} and the data type is {type(my_tuple)}")

print(type(my_tuple[0]))

print(type(my_tuple[3]))

print(type(my_tuple[-1]))

t = 1, 2, 3 # pcaking
print(type(t))

# t = ('5', )  # NOT (5)
# print(type(t))

print(f"length of the tuple is : {len(my_tuple)}")

print(f"the element apple present in {my_tuple.count("appleeeee")} times")

print(f"The first occurace of apple is at {my_tuple.index("apple")}")

# convert a list into tuple
list1 = [1,2,3,4,]
print(f"list one is {list1} and its type is {type(list1)}")

tupleConvertedFromList = tuple(list1)
print(f"list one is after converted to tuple {tupleConvertedFromList} and its type is {type(tupleConvertedFromList)}")


# slicing
print(my_tuple[::1])


a, b, c = t # unpacking
print(a, b, c)