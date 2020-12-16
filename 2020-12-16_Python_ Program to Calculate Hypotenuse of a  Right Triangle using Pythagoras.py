#Python program to side of a triangle using Pythagorean Theoream-12th December
# c^2 = a^2+ b2
# find the Hypotenuse of a right triangle
import math
def squareval(length):
    sq = float(length)*float(length)
    print("The Square of The Side is :",sq)
    return sq

def pythagorean(sidea,sideb):
    sidec = sidea+sideb
    hypotenuse =math.sqrt(sidec)
    print("The Hypotenuse of the 2 sides is :",hypotenuse)

## Input the Length of the sides a, and b

sidea = input(" Enter The  First side <a> : ")
sideb = input(" Enter The  First side <b> : ")

# get the Square of both sides:
a = squareval(sidea)
b =squareval(sideb)

##put the Square values of a, b intro the Pythagoras functions
pythagorean(a, b)
