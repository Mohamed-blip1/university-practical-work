def ex_1():
    import math

    def racine_et_log(x):
        if x <= 0:
            return "Le nombre doit etre strictement positive."

        return math.sqrt(x), math.log(x)

    # print(racine_et_log(2))

    def trigo(angle):
        return math.sin(angle), math.cos(angle), math.tan(angle)

    # print(trigo(math.pi))

    def distance_points(x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    # print(distance_points(1, 2, 4, 6))


# ex_1()


def ex_2():
    import random

    def lancer_de():
        return random.randint(1, 6)

    # print(lancer_de())

    def tirer_liste_aleatoire(n, a, b):
        return [random.randint(a, b) for _ in range(n)]

    # print(tirer_liste_aleatoire(5, 1, 5))

    def choisir_element(l):
        if len(l) == 0:
            return "Error: La list est vide."

        return random.choice(l)

    # print(choisir_element([1, 2, 3, 4]))

    def melanger_list(l):
        nl = l.copy()
        random.shuffle(nl)

        return nl

    l = [1, 2, 3, 4]

    # print(melanger_list(l))


# ex_2()


def ex_3():
    import os

    def repertoir_courant():
        return os.getcwd()

    # print(repertoir_courant())

    def contenu_repertoire(chemin):
        return os.listdir(chemin)

    # print(contenu_repertoire("some"))

    def fichier_existe(chemin):
        return os.path.exists(chemin)

    # print(fichier_existe("some"))

    def creer_dossier(nom_dossier):
        if os.path.exists(nom_dossier):
            return f"Error: '{nom_dossier}' dossier deja exist."

        else:
            os.makedirs(nom_dossier)
            return f"'{nom_dossier}' dossier a ete cree avec succes."

    # print(creer_dossier("else"))

    def compter_fichiers(chemin):
        if not os.path.exists(chemin):
            return 0

        items = os.listdir(chemin)
        fichiers = [f for f in items if os.path.isfile(os.path.join(chemin, f))]

        return len(fichiers)

    # print(compter_fichiers("some"))


# ex_3()
