# if : it will chevk the true condtion and executes the code block 

# temperature = int(input("Enter temparature: "))
# if temperature > 30:
#     print("It's hot outside!")
# else:
#     print("It is not soo bot outside") 

# balance = 50
# if balance >= 100:
#     print("Purchase approved.")
# else:
#     print("Insufficient funds.")

# marks = 8
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >=65:
#     print("Grade c")    
# else: # it will not accept any condition
#     print("Grade: D")

age = 20
citizen = True
indian = 'yes'

# if age >= 18:
#     print("Age is greater than 18")
#     if citizen:
#         print("Eligible to vote.")
#     else: 
#         print("Not eligible to vote.. since he is not a citizen")    

# age = 17
# if age < 18:
#     pass # it will let the code pass

# age = 11
# print("Adult" if age >= 18 else "Minor")

# if age >= 18 and citizen and indian == 'no': # both needs to be true if AND is there 
#     print("Eligible to vote.")
# else:
#     print("Note eligble to vote")    

# print("*****"*30)

# day = input("enter a day: ")
# if day == "Saturday" or day == "Sunday":
#     print("Weekend!")
# else:
#     print("week day...")

# raining = 'yes'

# if not raining == 'no':
#     print("Go for a walk.")

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits and 'apple'  in fruits:
    print("We have bananas and apples!")

if "mango" not in fruits:
    print("No mangoes available.")