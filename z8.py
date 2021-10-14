def zad8():
    list = []
    while(len(list)<5):
        liczba = int(input("podaj liczbę: "))
        list.append(liczba)
        print(tuple(list))
print(zad8())