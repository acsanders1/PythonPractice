# This script computes the total amount for an order of boxes of chips
# costing 20.00 each for the first 50, and 15.50 each thereafter

num = input("How many boxes of chips? ")

if num <= 50:
    total = num * 20.00
else:
    first = 50 * 20.00
    extra = (num - 50) * 15.50
    total = first + extra
print "Total:", total

    
