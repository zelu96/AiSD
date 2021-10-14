def zad2(x, y):
    x = x[0].upper()
    y = y.capitalize()
    return print(x + '. ' +y)
def wizytowka(imie,nazwisko,zad2):
    return zad2(imie,nazwisko)

imie="sylwester"
nazwisko="zelechowski"
print(wizytowka(imie,nazwisko,zad2))
