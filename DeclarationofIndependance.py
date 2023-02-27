#Programmer: Lucas Campbell
# Date: 2/21/2023
# Program: Navigation


# This function will take the input of your house and it will tell you how far away it is from your current location.


# Import libraries here
import random
import time	


# Show loading message
print("Navigation Services 1.0 is loading...")
time.sleep(3)
print("Navigation has loaded successfuly.")
time.sleep(1)

def getDistanceToHouse():
	# Get house distance from user and store as a variable
	houseAddress = input("What is the address of your house? ")


	# Calculating distance to house
	houseDistance = random.randint(1,200)

	# Tell user how far their house is
	time.sleep(1)
	print("Your house located at " + houseAddress + " is currently " + str(houseDistance) + " miles away.")
	time.sleep(1)


def generateRandomMiles():
	# This function generates a random number for use in the getDirections function
	randomMiles = random.randint(1,5)
	return randomMiles


def getDirections():
	# Create list of possible driving manuevers to describe directions
	possibleManuevers = ["Left turn", "Right turn", "Slight left turn", "Slight right turn", "U-Turn", "Go straight"]

	# Create list of possible sentence joiners
	conjunctions = [" and ", " then "]
	
	# Update user
	print("Generating your directions now... please wait.")
	time.sleep(1)
	print("Directions have been successfully generated. Please follow the following directions carefully")

	# Show directions
	x = 0
	while x < 10:
		print(str(possibleManuevers[random.randint(0, len(possibleManuevers))-1]) + " for " + str(generateRandomMiles()) + " miles")
		print(conjunctions[random.randint(0, len(conjunctions))-1])
		x = x + 1
		time.sleep(1)

	time.sleep(1)
	print("You have reached your destination!")


# Call functions
getDistanceToHouse()
getDirections()
# Thank user for using navigation
print("Thank you for using the navigation system. Goodbye.")
