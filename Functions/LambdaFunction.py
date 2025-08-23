
def evenOdd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(evenOdd(10))    

evenOddLambda = lambda X, Y : "Both values are even" if X%2==0 and Y%2==0 else "Both values or one value must be an Odd"
print(evenOddLambda(10, 10))



# square = lambda x: x * x

# print(square)
# print(square())  # 25


add = lambda a, b : f"The sum of {a} and {b} are {a+b}"
print(add(10,50))


list1 = [1,6,8,2,5]

def sum(listEle):
    sum = 0
    for i in list1:
        sum = sum+i
    return sum    

sms = lambda lst : sum(lst)
print(sms(list1)) 


# find max num of a list

maxNo = lambda x : max(x)

print(maxNo([90,32,89,10]))