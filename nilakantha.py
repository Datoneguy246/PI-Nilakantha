import sys
from decimal import *

def main(sum):
    # Alternate between adding and subtracting
    ADDING = True
    # For the multiplication part of the series
    MULTIPLY = 2

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

        # print
        print(sum)

if len(sys.argv) != 1:
    print("Usage: python3 nilakantha.py")
else:
    getcontext().prec = 100
    # Start the series with a sum of 3
    main(Decimal(3))