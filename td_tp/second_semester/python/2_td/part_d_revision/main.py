#!/usr/bin/env python3


# Ex-10


def ecrire_lignes(nom_fichier, lignes):

    with open(nom_fichier, "w") as f:

        for i in lignes:
            f.write(i + "\n")


# liste = ["Hello", "My", "name"]
# ecrire_lignes("file.txt", liste)

import os


def lire_fichier(nom_fichier):

    if not os.path.exists(nom_fichier):
        return False

    with open(nom_fichier, "r") as f:

        return f.read()


# print(lire_fichier("file.txt"))


def lire_lignes(nom_fichier):

    if not os.path.exists(nom_fichier):
        return False

    liste = []

    with open(nom_fichier, "r") as f:
        return f.read().splitlines()

    return liste


# print(lire_lignes("file.txt"))


def ajouter_ligne(nom_fichier, ligne):

    if not os.path.exists(nom_fichier):
        return False

    with open(nom_fichier, "a") as f:
        f.write(str(ligne).strip() + "\n")

    return True


# print(ajouter_ligne("file.txt", "Mohamed\n"))

# Ex-11


def nombre_lignes(nom_fichier):

    n_lines = 0
    with open(nom_fichier, "r") as f:
        content = f.read()

        for c in content:
            if c == "\n":
                n_lines += 1
    return n_lines


# print(nombre_lignes("file.txt"))


def nombre_caracteres(nom_fichier):

    n_caracters = 0
    with open(nom_fichier, "r") as f:
        content = f.read()

        for c in content:
            n_caracters += 1

    return n_caracters


# print(nombre_caracteres("file.txt"))


def mot_le_plus_long(nom_fichier):

    long_word = ""

    with open(nom_fichier, "r") as f:
        words = f.read().splitlines()

        for word in words:
            if len(word) > len(long_word):
                long_word = word

    return long_word


# print(mot_le_plus_long("file.txt"))

# Ex-12


def compter_occurrence_mot(nom_fichier, mot):

    mot = mot.lower()

    counter = 0

    with open(nom_fichier, "r") as f:
        words = f.read().split()

        for word in words:
            if mot == word.lower():
                counter += 1

    return counter


print(compter_occurrence_mot("file.txt", "mohamed"))


def lignes_contenant(nom_fichier, mot):

    result = []

    with open(nom_fichier, "r") as f:

        lines = f.read().splitlines()

        for line in lines:
            if mot in line:
                result.append(line)

    return result


# print(lignes_contenant("file.txt", "amed"))


def filtrer_lignes_longues(nom_fichier, longueur_min):

    result = []

    with open(nom_fichier, "r") as f:

        lines = f.read().splitlines()

        for line in lines:
            if len(line) >= longueur_min:
                result.append(line)

    return result


# print(filtrer_lignes_longues("file.txt", 8))
