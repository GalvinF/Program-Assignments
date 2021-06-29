# Step 1: Open Grocery Dictionary
groceries = {"Chicken": "$1:59" , "Beef": "$1:99" , "Cheese": "$1:00" , "Milk": "$2.50", "Apples": "$1.25", "Oranges": "$1:30", "Cherries": "$1:40"}

# Step 2: Create a function that takes the price of two menu items and adds them together, returning the total sum.
def priceTotal(price1, price2):
    sum = (price1 + price2)
    print("The total price of Chicken and Beef is " + str(sum))
    
print(priceTotal(groceries.get("Chicken"), groceries.get("Beef")))

# Step 3: Create a function that finds the difference in price between two menu items.
def priceDifference(price1, price2):
    difference = (price1 - price2)
    print("The difference price of Beef and Chicken is " + str(difference))
    
print(priceDifference(groceries.get("Beef"), groceries.get("Chicken")))