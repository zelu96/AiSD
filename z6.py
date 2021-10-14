def petla():
    suma=0
    while suma<100:
        liczba=int(input("podaj liczbe:"))
        suma+=liczba
        print(suma)
        if (suma >100):
            return print("przekroczyłeś 100")
    return suma

print(petla())