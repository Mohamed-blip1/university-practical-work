#!/usr/bin/env python3


def ex_10():

    def ecrire_lignes(nom_fichier: str, lignes: list):

        with open(nom_fichier, "w") as f:
            for l in lignes:
                f.write(str(l) + "\n")

    # ecrire_lignes("some.txt", ["mohamed", "bouharti", 22])

    def lire_fichier(nom_fichier):
        import os

        if not os.path.exists(nom_fichier):
            return f"Error: '{nom_fichier}' n'exist pas."

        with open(nom_fichier, "r") as f:
            return f.read()

    print(lire_fichier("some.txt"))

    def lire_lignes(nom_fichier):
        import os

        if not os.path.exists(nom_fichier):
            raise FileNotFoundError(f"'{nom_fichier}' n'exists pas.")

        with open(nom_fichier, "r") as f:
            return f.read().splitlines()

    # print(lire_lignes("some.txt"))

    def ajouter_ligne(nom_fichier, ligne):

        import os

        if not os.path.exists(nom_fichier):
            raise FileNotFoundError(f"'{nom_fichier}' n'exist pas.")

        with open(nom_fichier, "a") as f:
            f.write(str(ligne) + "\n")

    # ajouter_ligne("some.txt", "Hey, My name is Mohamed.")
    # print(lire_fichier("some.txt"))


# ex_10()


def ex_11():

    def nombre_lignes(nom_fichier):

        with open(nom_fichier, "r") as f:
            return len(f.readlines())

    # print(nombre_lignes("some.txt"))

    def nombre_mots(nom_fichier):
        with open(nom_fichier, "r") as f:
            words = f.read().split()

            return len(words)

    # print(nombre_mots("some.txt"))

    def nombre_caracteres(nom_fichier):
        with open(nom_fichier, "r") as f:
            content = f.read()

            return len(content)

    # print(nombre_caracteres("some.txt"))

    def mot_le_plus_long(nom_fichier):
        with open(nom_fichier, "r") as f:
            words = f.read().split()

            if not words:
                return None

            return max(words, key=lambda a: len(a))

    # print(mot_le_plus_long("some.txt"))


# ex_11()


def ex_12():

    def compter_occurrence_mot(nom_fichier, mot):
        with open(nom_fichier, "r") as f:

            string = f.read()

            return string.count(mot)

    # print(compter_occurrence_mot("some.txt", "Mohamed"))

    def lignes_contenant(nom_fichier, mot):
        with open(nom_fichier, "r") as f:
            lines = f.readlines()

            return [x.strip() for x in lines if x.count(mot)]

    # print(lignes_contenant("some.txt", "is"))

    def filtrer_lignes_longues(nom_fichier, longueur_min):
        try:
            with open(nom_fichier, "r") as f:
                lines = f.readlines()

                return [x.strip() for x in lines if len(x) >= longueur_min]

        except FileNotFoundError:
            return "Error: File Not Found."

    print(filtrer_lignes_longues("some.txt", 3))


ex_12()
