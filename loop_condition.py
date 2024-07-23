# Python Loop Statements - Assignment 2

# Task 1 - Infinite loop with user input break statement
fav_creature = True

while fav_creature:
    user = input("Can you guess my favorite creature that lives in the ocean?")
    if user == "Shark":
        break
    if user == "shark":
        break

# Task 2 - Loop that terminates after 5 iterations and prints which iteration it is on

guests = []

while len(guests) < 5:
    print("Welcome to my home, come in and grab a drink")
    guests.append('person')
    print("There are", len(guests), "people in my house right now")