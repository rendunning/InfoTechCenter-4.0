# Programmer: Lauren Dunning
# Date: 1.20.2023
# Program: InfoTechCenter Upgrades

"""
Our Welcome screen will start out program letting drivers know that the InfoTechCenter is loading
"""

#Import Libraries Here
import time
import sys

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