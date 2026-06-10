#Ximorra Jackson
#06/09/26
#P1HW2
# this assignment lets us on our own to calculate numbers

#This program calculates and displays travel expenses


print("----------This program calculates and displays travel expenses----------")

print()
print("Enter Budget:")
budget = float(input())
print("Enter your travel Destination:")
destination = input()   
print("how much do you expect to spend on gas?")
gas = float(input())
print("Approximately,how much will you need for accomodations/hotel?")
accomodations = float(input())
print("Last, how much do you need for food?")
food = float(input())
print("---------Travel Expenses---------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accommodation:", accomodations)
print("Food:", food)
print("Remaining Balance:", budget - (gas + accomodations + food))