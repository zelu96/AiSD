def rok_urodzenia(dwie_pierwsze, dwie_ostatnie, wiek):
    rok = str(pierwsze) + str(ostatnie)
    return int(rok) - wiek


pierwsze = 20
ostatnie = 21
wiek = 25
print(rok_urodzenia(pierwsze, ostatnie, wiek))