# Steps 2-4: Dictionary Practice
groceries = {"Chicken": "$1:59" , "Beef": "$1:99" , "Cheese": "$1:00" , "Milk": "$2.50"}
movies = {"A Quiet Place": "Thriller" , "Avengers: Endgame": "Action" , "The Martian": "Sci-Fi" , "Dumb and Dumber": "Comedy"}

chicken_price = groceries["Chicken"]
print(chicken_price)

beef_price = groceries["Beef"]
print(beef_price)

cheese_price = groceries["Cheese"]
print(cheese_price)

milk_price = groceries["Milk"]
print(milk_price)

a_quiet_place_genre = movies["A Quiet Place"]
print(a_quiet_place_genre)

avengers_endgame = movies["Avengers: Endgame"]
print(avengers_endgame)

the_martian = movies["The Martian"]
print(the_martian)

dumb_and_dumber = movies["Dumb and Dumber"]
print(dumb_and_dumber)

# Step 5: Practice Updating a Dictionary
NBA_players = {"Lebron James": 23 , "Kevin Durant": 35}

NBA_players["Lebron James"] = 6
jersey_number = NBA_players["Lebron James"]
print(jersey_number)

NBA_players["Lebron James"] -= 17
jersey_number = NBA_players["Lebron James"]
print(jersey_number)

# Step 6: Make A New Dictionary Based on Slide Show Table
basketball_shoes = {"Jordan 13": 1 , "Yeezy": 8 , "Foam Posite": 10 , "Air Max": 5 , "SB Dunk": 20}

# Step 7: Update The New Dictionary And It's Stored Values Based On The Prompts And Print The Results
basketball_shoes["SB Dunk"] += 2

basketball_shoes["Yeezy"] -= 1

basketball_shoes["Jordan 13"] += 7
basketball_shoes["Yeezy"] += 7
basketball_shoes["Foam Posite"] += 7
basketball_shoes["Air Max"] += 7
basketball_shoes["SB Dunk"] += 7

basketball_shoes["Jordan 13"] -= 7
basketball_shoes["Yeezy"] -= 7
basketball_shoes["Foam Posite"] -= 7
basketball_shoes["Air Max"] -= 7
basketball_shoes["SB Dunk"] -= 7

print(basketball_shoes)

# Step 8: Add Three New Key: Value Pairs To  Dictionaries 
groceries = {"Chicken": "$1:59" , "Beef": "$1:99" , "Cheese": "$1:00" , "Milk": "$2.50", "Apples": "$1.25", "Oranges": "$1:30", "Cherries": "$1:40"}
movies = {"A Quiet Place": "Thriller" , "Avengers: Endgame": "Action" , "The Martian": "Sci-Fi" , "Dumb and Dumber": "Comedy" , "Beetlejuice": "Comedy & Fantasy" , "A Rear Window": "Mystery" , "The Godfather": "Crime & Drama"}
NBA_players = {"Lebron James": 23 , "Kevin Durant": 35 , "Steph Curry": 30 , "Kyrie Irving": 11 , "Klay Thompson": 11} 
print(groceries)
print(movies)
print(NBA_players)

# Step 9: Delete Any 2 Keys From  Dictionaries And Print The Results
del groceries["Chicken"]
del groceries["Beef"]
del movies["The Martian"]
del movies["A Rear Window"]
del NBA_players["Kyrie Irving"]
del NBA_players["Lebron James"]
print(groceries)
print(movies)
print(NBA_players)

# Lists Practice
# Steps 1-2 

citiesList = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(citiesList)

# Step 3
animalsList = ["dog", "cat", "horse", "giraffe", "elephant", "tiger", "penguin", "gorilla", "gazelle", "panda"]
print(animalsList)

# print my top 3 cities
print(citiesList[0])
print(citiesList[2])
print(citiesList[7])

# print first three cities in list
threeCities = citiesList[0:3]
print(threeCities)

# Step 5
citiesList[0]= "San Francisco"
citiesList[2]= "Brooklyn"
citiesList[7]= "Hollywood"
citiesList[4]= "Tampa"
print(citiesList)

citiesList.append("New Jersey")
citiesList.extend([ "Santa Cruz", "Selma" , "Chicago"])
citiesList.insert(7, "Washington D.C.")
print(citiesList)

# Step 6
citiesList.append("Oakland")
citiesList.extend("New York City")
citiesList.extend("Los Angeles")
citiesList.insert(0, "Miami")
print(citiesList)

# Step 7: Removing Cities
citiesList.pop(0)
citiesList.remove("Tampa")
print(citiesList)