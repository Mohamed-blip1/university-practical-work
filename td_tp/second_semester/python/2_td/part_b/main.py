def ex_5():
    import outils_math

    print(f"2^2 = {outils_math.carre(2)}")

    print(f"2^3 = {outils_math.cube(2)}")

    n = 2
    if outils_math.est_pair(n):
        print(f"'{n}' est pair")
    else:
        print(f"'{n}' est impair")

    l = [1, 1, 1]
    print(outils_math.somme_liste(l))


# ex_5()


def ex_6():
    from conversion import celsius_vers_fahrenheit, fahrenheit_vers_celsius

    print("1. celsius vers fahrenheit")
    print("2. fahrenheit vers celsius")

    try:
        choix = int(input("Entre un choix: "))
    except ValueError:
        print("Error: Veuillez Entre 1 ou 2.")
        return -1

    if 1 <= choix <= 2:
        val = float(input("Entre un valuer: "))

        if choix == 1:
            print(f"{val}C = {celsius_vers_fahrenheit(val)}F")
        else:
            print(f"{val}F = {fahrenheit_vers_celsius(val)}C")
    else:
        print("Veuillez Entre 1 ou 2.")


# ex_6()
