print("pression systolique")
print()
mesure_du_matin= float(input("mesure du matin: "))
mesure_du_midi= float(input("mesure du midi: "))
mesure_du_soir= float(input("mesure du soir: "))
print()
moyenne= (mesure_du_matin + mesure_du_midi + mesure_du_soir)/3
print("moyenne de la pression systolique", moyenne, "mmHg")
