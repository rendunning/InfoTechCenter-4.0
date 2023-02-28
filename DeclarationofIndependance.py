# Programmer: Lauren Dunning
# Date: 1.31.2023
# Program: InfoTech Center 4.0 - Gasoline

"""
We will create a Function that will tell us out Fuel Gauge level
    - Create a List with Gas Levels
    - Randomize and choose from the list to determine our gas level

Create a Functon to determine our closest Gas Station
    - Create a List of gas stations
    - Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
    - PrintGas level
    - Print Closest Gas Station
"""

# import libraries here
import random
from time import sleep


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", 'Quarter Tank', "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()


# List of Gas Stations Function

def listOfGasStations():
    gasStations = ["shell", "Costco", "Sam's Club", "Buc-ee's", "7/11", "Speedway", "Meijer"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


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
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a Quarter Tank and the closest gas station is", listOfGasStations, "which is",
              milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your has tank is a half of a tank full, which is plenty of gas to make it to your destinations today.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print(
            "Your gas tank is at three quarters of a tank which is plenty of gas to make it to your destination today.")
    else:
        print("Your gas tank is full - Yeah! - Congratulations")


gasLevelAlert()

# Programmer: Lucas Campbell
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
    houseDistance = random.randint(1, 200)

    # Tell user how far their house is
    time.sleep(1)
    print("Your house located at " + houseAddress + " is currently " + str(houseDistance) + " miles away.")
    time.sleep(1)


def generateRandomMiles():
    # This function generates a random number for use in the getDirections function
    randomMiles = random.randint(1, 5)
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
        print(str(possibleManuevers[random.randint(0, len(possibleManuevers)) - 1]) + " for " + str(
            generateRandomMiles()) + " miles")
        print(conjunctions[random.randint(0, len(conjunctions)) - 1])
        x = x + 1
        time.sleep(1)

    time.sleep(1)
    print("You have reached your destination!")


# Call functions
getDistanceToHouse()
getDirections()
# Thank user for using navigation
print("Thank you for using the navigation system. Goodbye.")

# Programmer: Lauren Dunning
# Date: 2/21/2023
# Program: Cruise Control

"""
This program will ask you what speed you would like to maintain
and turn off cruise control.
"""

from time import sleep


def engageCruiseControl():
    answer = input("Would you like to engage cruise control, yes or no: ").lower()
    if answer == "yes":
        speed = int(input("What speed would you like to cruise at: "))
        if speed > 75:
            print("Slow down buckaroo, that's faster than interstate highway speed limits. Try a different speed.")
        else:
            print("Now cruising at", speed, "MPH.\n")
            sleep(4)
            turnoff = input("Press X to turn off cruise control: ")
            if turnoff == "X":
                print("Cruise control has been disabled.")
            elif turnoff == "x":
                print("Cruise control has been disabled.")
            else:
                print("Cruise control is still active at", speed, "MPH.")
    elif answer == "no":
        print("Cruise control request cancelled.")
    else:
        print("Please enter yes or no.")


engageCruiseControl()

def systemRadio():
    # Define a dictionary of stations with genres and songs
    stations = {
        1: {
            "name": "Station 1",
            "genre": "Pop",
            "songs": ["'golden hour' by JVKE", "'Kill Bill' by SZA", "'As It Was' by Harry Styles"]
        },
        2: {
            "name": "Station 2",
            "genre": "Rock",
            "songs": ["'One' by Metallica", "'Numb' by Linkin park", "'Stairway to Heaven' by Led Zeppelin"]
        },
        3: {
            "name": "Station 3",
            "genre": "Hip Hop",
            "songs": ["'XXX Ft. U2' by Kendrick Lamar", "'Without Me' by Eminem", "'The Worst Guys' by Childish Gambino"]
        }
    }

    # Ask user if they want to turn on the radio
    user_input = input("Do you want to turn on the radio? (yes/no): ")

    # If user answers "yes", list the stations and ask them to choose one
    if user_input.lower() == "yes":
        print("Here are three different stations with different genres:")
        for number, details in stations.items():
            print(number, "-", details["name"], "-", details["genre"])
        station_choice = input("Please choose a station number (1-3): ")
        if station_choice.isdigit() and int(station_choice) in stations:
            chosen_station = stations[int(station_choice)]
            print("Playing a song from", chosen_station["name"])
            random_song = random.choice(chosen_station["songs"])
            print("Playing song:", random_song)
        else:
            print("Invalid station choice.")

    # If user answers "no", exit the program
    elif user_input.lower() == "no":
        print("Goodbye!")
        exit()

    # If user gives an invalid response, prompt them to try again
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

systemRadio()