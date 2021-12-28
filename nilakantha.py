import sys
from decimal import *
from time import sleep
from os.path import exists

def main(sum, i):
    # Alternate between adding and subtracting
    ADDING = True
    # For the multiplication part of the series
    MULTIPLY = 2 + i

    while True:
        # Sick calculations bro
        quotient = Decimal(4) / Decimal(MULTIPLY * (MULTIPLY + 1) * (MULTIPLY + 2))
        if ADDING:
            sum = sum + quotient
        else:
            sum = sum - quotient
    
        # Change the variables
        MULTIPLY = MULTIPLY + 2
        ADDING = not ADDING

        # Write to file
        f = open("pi.txt", "w")
        f.write(str(sum) + "?" + str(i))
        f.close()

        # print
        print(sum)

        # keep track of the iterations
        i = i + 1
        sleep(0.001)

getcontext().prec = 100

# Get last sum and it's term number (if it exists)
startSum = Decimal(3)
startI = 0
if exists("pi.txt"):
    f = open("pi.txt", "r")
    save = f.read()
    saveData = save.split('?', 1)
    startSum = Decimal(float(saveData[0]))
    startI = int(saveData[1])
    f.close()

# Start the series
main(startSum, startI)