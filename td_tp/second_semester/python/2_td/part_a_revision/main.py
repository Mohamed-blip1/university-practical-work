#!/usr/bin/env python3

import math


# Ex-1
def racine_et_log(x):

    return math.sqrt(x), math.log(x)


# print(racine_et_log(10))


def trigo(angle):
    return math.sin(angle), math.cos(angle), math.tan(angle)


# print(trigo(math.pi / 2))
# print(trigo(math.pi / 2))


def distance_points(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# print(math.cos(math.pi / 2))

# Ex-2

import random


def lancer_de():
    return random.randint(1, 6)


# print(lancer_de())


def tirer_list_aleatoire(n, a, b):

    return [random.randint(a, b) for i in range(n)]


# print(tirer_list_aleatoire(10, 0, 100))


def choisir_element(L: list):

    if not L:
        return None

    return random.choice(L)


# print(choisir_element(["mohamed", "Ali"]))


def melanger_list(L: list) -> list:

    nL = L.copy()

    random.shuffle(nL)

    return nL


nL = [1, 2, 3, 4]

# print(melanger_list(nL))

# print(nL)

# Ex-3

import sys


def infos_python():
    return sys.version, sys.platform


# print(infos_python())


def arguments_programme():
    return sys.argv


# print(arguments_programme())


def somme_arguments():

    s = 0

    for i in sys.argv:
        try:
            s += int(i)
        except ValueError:
            continue

    return s


# print(somme_arguments())

# Ex-4

import os


def repertoire_courant():
    return os.getcwd()


# print(repertoire_courant())


def contenu_repertoire(chemin):
    return os.listdir(chemin)


# print(contenu_repertoire(repertoire_courant()))


def fichier_existe(chemin):

    return os.path.exists(chemin)


# print(fichier_existe(repertoire_courant()))
# print(fichier_existe("/home/mohamed/"))


def creer_dossier(nom_dossier):
    if os.path.exists(nom_dossier):
        return False

    os.makedirs(nom_dossier)
    return True


# if creer_dossier("a"):
#     print("File created.")
# else:
#     print("Files already exist.")


def compter_fichiers(chemin):

    if not os.path.exists(chemin):
        return False

    dir_items = os.listdir(chemin)

    counter = 0
    for i in dir_items:
        if os.path.isfile(os.path.join(chemin, i)):
            counter += 1

    return counter


# print(compter_fichiers(os.getcwd()))
