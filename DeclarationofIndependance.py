# Programmer: Lauren Dunning
# Date: 2.08.2023
# Program: Weather Center Updates

# Import libraries here
import random

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

vehicleResponseSystem()