def ex_7():

    def division_securisee(a, b):

        try:
            return a / b

        except ZeroDivisionError:
            return "Error: Ne peut pas diviser par zero."

    # print(division_securisee(1, 0))

    import math

    def racine_seurisee(x):
        try:
            return math.sqrt(x)
        except ValueError:
            return "Error: Impossible de calculer la racine carre d'un nombre negatif."

    # print(racine_seurisee(0))

    def conversion_entier(texte):

        try:
            return int(texte)
        except ValueError:
            return f"Error: '{texte}' n'est pas un entier."
        except TypeError:
            return f"Error: {texte} n'est pas un texte."

    # print(conversion_entier([1, 2]))
    # print(conversion_entier("1.2"))
    # print(conversion_entier("2"))


# ex_7()


def ex_8():

    def lire_age(age):

        if type(age) != int:
            raise TypeError("Error: L'age doit etre un nomber entier.")

        if age < 0:
            raise ValueError("Error: L'age ne peut pas etre negatif.")

        return age

    # try:
    #     a = lire_age(-12)
    # except Exception as e:
    #     print(e)

    def lire_note(note):

        if not 0 <= note <= 20:
            raise ValueError("Error: La note doit etre entre 0 et 20.")

        return note

    # try:
    #     a = lire_note(22)
    # except Exception as e:
    #     print(e)

    def moyenne_notes_valides(notes):

        if not notes:
            return 0.0

        somme = 0

        for n in notes:

            if type(n) != float:
                raise TypeError("Error: La note doit etre un entier.")

            if not 0 <= n <= 20:
                raise ValueError("Error: La note doit etre entre 0 et 20.")

            somme += n

        return somme / len(notes)

    # try:
    #     print(moyenne_notes_valides([1, 2, 3, "s", 23]))
    # except Exception as e:
    #     print(e)


# ex_8()


def ex_9():

    def element_liste(l, indice):

        try:
            return l[indice]
        except IndexError:
            raise IndexError("Error: d'indice invalide.")

    l = [1, 2, 3]

    # try:
    #     print(element_liste(l, -1))
    # except Exception as e:
    #     print(e)

    def inverse_nomber(x):

        try:
            return 1 / x
        except ZeroDivisionError:
            return "Error: L'inverse de zero n'est pas defini."

    # print(inverse_nomber(0))

    def traiter_liste_nombres(l):

        if type(l) != list:
            raise TypeError(f"{l} n'est pas une liste.")

        somme = 0

        for i in l:
            try:
                somme += float(i)
            except (ValueError, TypeError):
                continue

        return somme

    ma_liste = ["10", "abc", "5.5", None, "20"]
    print(traiter_liste_nombres(ma_liste))


ex_9()
