import sys
from decimal import *
from time import sleep
from os.path import exists

def main(sum, i, add):
    # Alternate between adding and subtracting
    ADDING = add
    # For the multiplication part of the series
    MULTIPLY = Decimal(2 * (i+1))

    while True:
        # Sick calculations bro
        quotient = Decimal(4) / Decimal(MULTIPLY * (MULTIPLY + 1) * (MULTIPLY + 2))
        if ADDING:
            sum = sum + quotient
        else:
            sum = sum - quotient

        # keep track of the iterations
        i = i + 1
        # Change the variables
        MULTIPLY = MULTIPLY + 2
        ADDING = not ADDING

        # Write to file
        if i % 100 == 0:
            f = open("pi.txt", "w")
            f.write(str(sum) + "?" + str(i) + "?" + str(ADDING))
            f.close()
            sleep(0.001)

        # print
        print(sum)

getcontext().prec = 100

# Get last sum and it's term number (if it exists)
startSum = Decimal(3)
startI = 0
startAdd = True
if exists("pi.txt"):
    f = open("pi.txt", "r")
    save = f.read()
    saveData = save.split('?', 2)
    startSum = Decimal(saveData[0])
    startI = int(saveData[1])
    startAdd = saveData[2] == "True"
    f.close()

# Start the series
main(startSum, startI, startAdd)