# Programmer: Lauren Dunning
# Date: 1.20.2023
# Program: InfoTechCenter Upgrades


# This function will take the input of your house and it will tell you how far away it is from your current location.


# Import libraries here
import random
import time	


while x != 20:
    x += 1
    b = ("\033[1;33;35m InfoTechCenter is loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;35m Done!')



# Date: 1.31.2023
# Program: InfoTech Center 4.0 - Gasoline
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

# Determine Gas Level & Closest gas station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuarterTank = round(random.uniform(1, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOUR TANK IS EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("*****Warning*****")
        sleep(1)
        print("Your gas tank is extremely low; checking Google Maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is", listOfGasStations(),"which is",milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is" ,listOfGasStations, "which is" ,milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your has tank is a half of a tank full, which is plenty of gas to make it to your destinations today.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank which is plenty of gas to make it to your destination today.")
    else:
        print("Your gas tank is full - Yeah! - Congratulations")
        
gasLevelAlert()
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
