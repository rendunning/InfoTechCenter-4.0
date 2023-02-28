# Programmer: Lauren Dunning
# Date Merged: 2.13.2023
# Merged Welcome Screen, Gasoline, and Weather - Stable

# Import Libraries Here
import time
import sys
import random
from time import sleep

# Date: N/A
# Program: Welcome Screen

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
    sys.stdout.write('\r' + b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;35m Done!\n')

# Date: 1.31.2023
# Program: Gasoline

"""
We will create a Function that will tell us our fuel gauge level
    - Create a List with Gas Levels
    - Randomize and choose from the list to determine our gas level

Create a Functon to determine our closest Gas Station
    - Create a List of gas stations
    - Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
    - Print Gas level
    - Print Closest Gas Station
"""


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", 'Quarter Tank', "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()


# List of Gas Stations Function

def listOfGasStations():
    gasStations = ["Shell", "Costco", "Sam's Club", "Buc-ee's", "7/11", "Speedway", "Meijer"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


# Determine Gas Level & Closest gas station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25), 2)
    milesToGasStationQuarterTank = round(random.uniform(1, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOUR TANK IS EMPTY***")
        sleep(1)
        print("Calling Emergency Contact.\n")
    elif gasLevelIndicator == "Low":
        print("*****Warning*****")
        sleep(1)
        print("Your gas tank is extremely low; checking Google Maps for the closest gas station.\n")
        sleep(1)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away.\n")
    elif gasLevelIndicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Your gas tank is at a quarter tank and the closest gas station is", listOfGasStations(), "which is",
              milesToGasStationQuarterTank, "miles away.\n")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full which is plenty of gas to make it to your destinations today.\n")
    elif gasLevelIndicator == "Three Quarter Tank":
        print(
            "Your gas tank is at three quarters of a tank which is plenty of gas to make it to your destination today.\n")
    else:
        print("Your gas tank is full - Yeah! - Congratulations\n")


# Date: 2.08.2023
# Program: Weather

# Create weather condition in a list and choose it randomly
def weather():
    weatherForecast = ["snow.", "blizzard.", "rain", "foggy", "windy", "icy", "sunshine,"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


# Variable to call weather() once in our VRS()
weatherAlert = weather()


# VRS() to respond to the weather condition
def vehicleResponseSystem():
    if weatherAlert == "snow.":
        print("\nNWS has changed your alarm by 15 minutes because of the weather forecast of", weatherAlert, )
        print("VRS has been engaged only allowing your vehicle to go 45 MPH")
    elif weatherAlert == "blizzard.":
        print("\nNWS has changed your alarm by 30 minutes because of the weather forecast of", weatherAlert, )
        print("VRS has been engaged only allowing your vehicle to go 35 MPH")
    elif weatherAlert == "icy":
        print("\nNWS has changed your alarm by 60 minutes because of the weather forecast of", weatherAlert,
              "conditions; please drive carefully.")
        print("VRS has been engaged only allowing your vehicle to go 25 MPH")
    elif weatherAlert == "rain":
        print("\nNWS is calling for", weatherAlert, ",please drive carefully.")
    elif weatherAlert == "foggy":
        print("\nNWS is calling for", weatherAlert, "conditions; please drive carefully.")
    elif weatherAlert == "windy":
        print("\nNWS is calling for", weatherAlert, "conditions; please drive carefully.")
    else:
        print("\nNWS is calling for", weatherAlert, "drive safely and have a wonderful day.")


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


# Call functions here
print("Checking gas tank levels...\n")
sleep(1)
gasLevelAlert()
print("Checking VRS system conditions...")
sleep(1)
vehicleResponseSystem()
sleep(1)
systemRadio()
