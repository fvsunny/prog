def niveau_acidite(pH) :
    if pH == 7 :
        return("neutre")
    if pH < 7 :
        return("acide")
    if pH > 7 :
        return("basique")


print(f"Une solution avec un pH de 5 est : {niveau_acidite(5)}")
print(f"Une solution avec un pH de 7 est : {niveau_acidite(7)}")
print(f"Une solution avec un pH de 10 est : {niveau_acidite(10)}")