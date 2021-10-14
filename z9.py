def zad9():
    dni=['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek','Sobota', 'Niedziela']
    liczba = int(input('Podaj liczbę '))
    return dni[liczba-1]
print(zad9())