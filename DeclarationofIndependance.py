# Programmer: Lauren Dunning
# Date: 1.20.2023
# Program: InfoTechCenter 4.0

#Import Libraries Here
import time
import sys
import random
from time import sleep

"""
Our Welcome screen will start out program letting drivers know that the InfoTechCenter is loading
"""

print('\n\033[1;34;48m Welcome to InfoTechCenter')

x = 0
a = 0

time.sleep(2)
print('')

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


# Program: Gasoline

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


# Program: Gas Level Function
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


# Program: Weather


# Create weather condition in a list and choose it randomly
def weather():
	weatherForecast = ["snow", "blizzard", "rain", "foggy", "windy", "icy", "sunshine"]
	weatherCondition = random.choice(weatherForecast)
	return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()

# VRS() to respond to the weather condition
def vehicleResponseSystem():
	if weatherAlert == "snow":
		print("\nNWS has changed your alarm by 15 minutes because of the weather forecast of",weatherAlert,".")
		print("VRS has been engaged only allowing your vehicle to go 45 MPH")
	elif weatherAlert == "blizzard":
		print("\nNWS has changed your alarm by 30 minutes because of the weather forecast of",weatherAlert,".")
		print("VRS has been engaged only allowing your vehicle to go 35 MPH")
	elif weatherAlert == "icy":
		print("\nNWS has changed your alarm by 60 minutes because of the weather forecast of",weatherAlert,"conditions, please drive carefully.")
		print("VRS has been engaged only allowing your vehicle to go 25 MPH")
	elif weatherAlert == "rain":
		print("\nNWS is calling for",weatherAlert,",please drive carefully.")
	elif weatherAlert == "foggy":
		print("\nNWS is calling for",weatherAlert,"conditions, please drive carefully.")
	elif weatherAlert == "windy":
		print("\nNWS is calling for",weatherAlert,"conditions, please drive carefully.")
	else:
		print("\nNWS is calling for",weatherAlert,",drive safely and have a wonderful day.")


#Call functions here
gasLevelAlert()
vehicleResponseSystem()

