def densite(masse, volume):
   if masse < 0 :
    raise ValueError("masse must be positive")
   if volume <= 0 :
    raise ZeroDivisionError("volume must be strictly positive")
   return masse/volume

print(densite(7,2))


