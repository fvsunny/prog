def aire_rectangle(longueur, largeur):
    aire = longueur * largeur
    return aire

def volume_prisme(longueur, largeur, hauteur):
    volume = aire_rectangle(longueur, largeur) * hauteur
    return volume

print(volume_prisme(5, 3, 4))