#!/usr/bin/env python3


# Ex-7


def division_securisee(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# print(division_securisee(1, 0))

import math


def racine_securisee(x):

    try:
        return math.sqrt(x)
    except ValueError:
        raise ValueError("Error racine d'un nombre negative")


# print(racine_securisee(-2))


def conversion_entier(texte):
    try:
        return int(texte)
    except TypeError:
        return "Error: input doit etre string."
    except ValueError:
        return "Error: Le texte doit contain des Nombres."


# print(conversion_entier("2sd"))

# Ex-8


def lire_age(age):

    try:
        age = int(age)

        if age > 0:
            return age
        raise ValueError("Error: L'age doit etre positive")
    except:
        raise ValueError("Error: age doit etre un Nombre.")


# print(lire_age())


def lire_note(note):
    if 0 <= note <= 20:
        return note
    raise ValueError("Error: note doit etre entre 0 et 20.")


# print(lire_note(float(input("Enter note: "))))


def moyenne_notes_valides(notes):
    somme = 0

    for i in notes:
        try:
            somme += lire_note(i)
        except TypeError:
            raise TypeError("Error: Une note est invalide.")

    return somme / len(notes)


# print(moyenne_notes_valides([20, 10]))

# Ex-9


def element_liste(liste, indice):

    try:
        return liste[indice]
    except IndexError:
        return "Error: Indice depace."


# print(element_liste([1, 2], 4))


def inverse_nombre(x):

    try:
        return 1 / x
    except ZeroDivisionError:
        return "Error: Division pare zero"


def traiter_liste_nombres(liste):

    somme = 0

    for i in liste:

        try:
            somme += float(i)

        except (ValueError, TypeError):
            continue

    return somme


# print(traiter_liste_nombres(["1", "1", "a", "1", [2]]))
