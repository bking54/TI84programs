# V 0.1
#Use 2 Ender eyes to locate the stronghold

import math

print("Record 1st throw position")
print("")

a1 = int(input("X= "))
b1 = int(input("Y= "))

print("")
print("Throw eye. Record hovering position")
print("")

a2 = int(input("X= "))
b2 = int(input("Y= "))

print("")
print("Record 2nd throw position")
print("")

c1 = int(input("X= "))
d1 = int(input("Y= "))

print("")
print("Throw eye. Record hovering coords")
print("")

c2 = int(input("X= "))
d2 = int(input("Y= "))

#Transform into linear eq
slope1 = (b1 - b2) / (a1 - a2)
yint1 = b1 - (slope1 * a1)
slope2 = (d1 - d2) / (c1 - c2)
yint2 = d1 - (slope2 * c1)
print("LINE 1: ", str(slope1), "X +" + str(yint1))
print("LINE 2: ", str(slope2), "X +" + str(yint2))
#Solve for x then y
if slope1 == slope2:
    print("Try Again.")
elif slope1 > slope2:
    finalx = (yint2 - yint1) / (slope1 - slope2)
else:
    finalx = (yint1 - yint2) / (slope2 - slope1)
finaly = yint2 + (slope2 * finalx)

print("")
print("Approx Stronghold Position: ", round(finalx, 0), ", ", round(finaly, 0))
print("")
