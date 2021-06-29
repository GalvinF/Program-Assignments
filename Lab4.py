def rectangleArea(width,height):
    area = width * height
    return area

print(rectangleArea(4,6))
print(rectangleArea(7,9))

rectOne = rectangleArea(4,6)
rectTwo = rectangleArea(7,9)

print(rectOne + rectTwo)

# Official lab starts now
#Calculate total of two tiems
groceries = {"Chicken": 1.59 , "Beef": 1.99 , "Cheese": 1.00 , "Milk": 2.50}
shoes = {"Jordan 13": 1 , "Yeezy": 8 , "Foam Posite": 10 , "Air Max": 5 , "SB Dunk": 20}

"Chicken", "Beef", "Cheese", "Milk"

def total_price(item1, item2):
    item1_price = groceries[item1]
    item2_price = groceries[item2]
    price = (item1_price + item2_price)

    return price

print("The price of Chicken and Cheese is: " + str(total_price("Chicken", "Cheese")))
print("The price of Beef and Milk is: " + str(total_price("Beef", "Milk")))

#Calculate difference of two items
def price_difference(item1, item2):
    item1_price = groceries[item1]
    item2_price = groceries[item2]

    if item1_price > item2_price:
        difference = item1_price - item2_price
    else:
        difference = item2_price - item1_price

    return difference

print("The difference between Chicken and Cheese is: " + str(price_difference("Chicken", "Cheese")))
print("The difference between Beef and Milk is: " + str(price_difference("Beef", "Milk")))
