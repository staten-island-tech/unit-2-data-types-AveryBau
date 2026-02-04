""" import turtle
from turtle import *
t = Turtle()
 """
""" x = 3 
y = float(3)
print(x,y) """

""" values = [1,2,23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" sentence = input("please enter a sentence")
if sentence == (input):
    print(input)
    for i in input:
        print(i) """
    

""" x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" name = ALice
age = 30 
print(f"my name is {name} and I am {age} years old") """

""" number = int(input("give me number"))
if number >= 21:
    print("can vote and gamble")
elif(number >= 18):
    print("can vote but not gamble")
else:
    print("have a juice box kid")

#18 and 25
#3, 5,
#if number isFactor of 18 and if number isFactor of 25 """

""" temp = 55
if (temp > 40 and temp < 60):
    print("light jacket needed")
elif (temp < 20 or temp > 90):
    print("extreme") """

""" x = True
print(not(x))

User:{}
if not User:
    print("please log in")

def is_animal_allowed(is_herbivore, weight, is_predator):
    if(is_herbivore or weight < 50) and not is_predator:
        return "The animal is allowed in the open area."
    else:
        return "The animal is not allowed in the open area." """
    
""" def discount(isMember, age, isResident):
    if(isMember or isResident): 
        print("discount granted")
age = int(input("enter age"))
if (age < 12 or age > 65):
    print("discount granted")
else: 
    print("NO DISCOUNT FOR YOU")
 """

""" animals = [
    {"name": "Leo", "species": "Lion", "weight": 420}
] """

""" bill = float(input("enter bill"))
tip = float("how much would you like to tip?")
if bill > 0:
    print(tip)
if tip >= 0:
    print(bill*tip+bill)

sentence = input() """

""" 
sentence = input("please type a sentence")
if sentence """

""" number = int(input("give me a number"))
if number == input / 2:
    print("even")
else:
    print("odd") """


""" x = "this is a thing"
y = x.count("")
print(y) """


bill = int(input("what bill"))
service = input("good, bad, okay, great")
def getTip(bill, service):
       if bill >0:
        print(service)
        if service == ("good"):
            print(.20)
        if service == ("bad"):
            print(0)
        if service == ("okay"):
            print(.15)
        if service == ("great"):
            print(.25)