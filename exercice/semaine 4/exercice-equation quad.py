import math

a = 1
b = 5
c = 6
x = (b**2) - (4 * a * c)
if a == 0 :
    raise ZeroDivisionError("a must be different than 0")
if x > 0 :
    y1 = (-b + math.sqrt(x)) / (2 * a)
    y2 = (-b - math.sqrt(x)) / (2 * a)
    print(f"il y a 2 solutions possibles : {y1} et {y2}")
elif x == 0 :
    y1 = (-b + math.sqrt(x)) / (2 * a)
    print(f"il y a une seule solution (racine double) : {y1}")
else :
    print("Il n'y a pas de solution réelle pour ces valeurs de a, b et c")

print()
