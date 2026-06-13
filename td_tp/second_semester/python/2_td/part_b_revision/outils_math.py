#!/usr/bin/env python3


def carre(x):
    return x**2


def cube(x):
    return x**3


def est_pair(n):
    return n % 2 == 0


def somme_liste(liste):
    counter = 0

    for i in liste:
        counter += i

    return counter
