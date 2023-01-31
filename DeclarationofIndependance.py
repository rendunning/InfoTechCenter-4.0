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

print(gasLevelGauge())

# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gaslevelGauge()
 
# List of Gas Stations Function
 
def listOfGasStations():
    gasStations = ["shell", "Costco", "Sam's Club", "Buc-ee's", "7/11", "Speedway", "Meijer"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby
