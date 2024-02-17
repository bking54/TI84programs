# V 0.2
#Use fewer Ender eyes to locate the stronghold

import math

#Objects
class LinearEq:
    def __init__(self, id, x1, y1, x2, y2):
        self.id = id
        self.slope = (y1 - y2) / (x1 - x2)
        self.yint = y1 - (self.slope * x1)
    def __str__(self):
        return str(self.slope) + "x + " + str(self.yint)

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Vars
index = 0
loop = True
linearEquations = []
approximations = []

#Methods
def getIntersect(line1, line2):


#Start loop
while loop:

    #Collect positions for first throw and hover

    #Extract linear eq

    #Store linear eq

    #Make approximation, if possible

    #Display results

    #Exit loop if done
    print("")
    print("Enter more positions? (0 to exit, 1 to continue)")
    print("")
    quit = input()
    if quit == 0:
        loop = False

#Print final results
