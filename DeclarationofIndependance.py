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
            print("Now cruising at",speed,"MPH.\n")
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