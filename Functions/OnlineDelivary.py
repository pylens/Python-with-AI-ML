def selectFood(item):
    return f"selected {item}"

def processPayment(amount):
    return f"Payment of $ { amount} sucesfully"

def delivarFood(item):
    return f"delivered {item} to your address"

def OrderFood(item, price):
    step1 = selectFood(item)
    step2 = processPayment(price)
    step3 = delivarFood(item)

    return f"Ordered summary\n{step1}\n{step2}\n{step3}"

print("******"*30)
print(OrderFood("Boba Drink", 299))