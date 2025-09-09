# sentence = "Python is fun to learn"
# words = sentence.split()  
# print(words)  # ['Python', 'is', 'fun', 'to', 'learn']

# csv_data = "John,Doe,25,NewYork"
# fields = csv_data.split(',', 20)
# print(fields)  

# words = ['Python', 'is', 'awesome']
# sentence = " ".join(words)
# print(sentence)  # Python is awesome

# paths = ["home", "user", "documents"]
# full_path = "/".join(paths)
# print(full_path)  # home/user/documents

text = "I like Java. Java is powerful."
new_text = text.replace("Java", "Python")
print(new_text)  # I like Python. Python is powerful.

limited = text.replace("Java", "Python", 1)
print(limited)  # I like Python. Java is powerful.

print("*"*50)
quote = "Knowledge is power"
index = quote.find("power")
print(index)  # 13

missing = quote.find("money")
print(missing)

print("*"*50)

name = "Alice"
age = 25
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)  # My name is Alice and I am 25 years old.

print("Hello {0}, you scored {1}%".format("Bob", 92))
print("Hello {name}, you scored {score}%".format(name="Charlie", score=88))
