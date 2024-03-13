age = int(input("provide me an age "))
day = input("provide me a day")

price = 12 if age>= 18 else 8

if day == "Wednesday":
    price -= 2

print(" ticket price is $",price)