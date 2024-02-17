#Quadratic Formula

import math

print("Enter Coefficients: ")
a = float(input("X^2 Coefficient: "))
b = float(input("X Coefficient: "))
c = float(input("Constant: "))
print("")

realtest = b * b - (4 * a * c)
if a == 0:
    print("This is not a quadratic.")
elif realtest > 0:
    x1 = round(((b * -1) + math.sqrt(realtest)) / (2 * a), 5)
    x2 = round(((b * -1) - math.sqrt(realtest)) / (2 * a), 5)
    print("There are two real roots:")
    print(x1, ", ", x2)
elif realtest < 0:
    if b == 0:
        xreal = 0
    else:
        xreal = round((b * -1) / (2 * a), 5)
    ximag = round(math.sqrt(-realtest) / (2 * a), 5)
    x1 = str(xreal) + "+" + str(ximag) + "i"
    x2 = str(xreal) + "-" + str(ximag) + "i"
    print("There are two complex roots:")
    print(x1, ", ", x2)
else:
    if b == 0:
        x = 0
    else :
        x = round((b * -1) / (2 * a), 5)
    print("There is one real root:")
    print(x)