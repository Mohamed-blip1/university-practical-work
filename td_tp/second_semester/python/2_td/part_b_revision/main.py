#!/usr/bin/env python3

import outils_math

# print(outils_math.carre(2))
# print(outils_math.cube(2))
# print(outils_math.est_pair(2))
# print(outils_math.somme_liste([1, 2, 3, 4, 5]))

import conversion

print("1. celsuis vers fahrenheit")
print("2. fahrenheit vers celsuis ")

choice = int(input("choix: "))

value = float(input("Entre la valuer: "))
result = 0

match choice:
    case 1:
        result = conversion.celsius_vers_fahrenheit(value)
    case 2:
        result = conversion.fahrenheit_vers_celsius(value)

print(result)
