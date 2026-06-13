import sys


def lire_notes_fichier(nom_fichier):
    try:
        with open(nom_fichier, "r") as f:
            lines = f.read().split()

            dic = {}

            for line in lines:
                key, value = line.split(";")
                dic[key] = int(value)

            if not dic:
                return ("Error: Empty File.", -1)

            return (dic, True)

    except FileNotFoundError:
        return (f"Error: File name '{nom_fichier}' does not exist.", False)
    except ValueError:
        return ("Error: Unexpected values in file.", False)


def moyenne_classe(nom_fichier):
    val, state = lire_notes_fichier(nom_fichier)

    if not state or state == -1:
        return (val, False)

    values = val.values()

    return (sum(values) / len(values), True)


def meilleure_note(nom_fichier):

    val, state = lire_notes_fichier(nom_fichier)

    if not state or state == -1:
        return (val, None, False)

    max_point = max(val.values())
    best_students = [k for k, i in val.items() if i == max_point]

    return (best_students, max_point, True)


def admis(nom_fichier):
    val, state = lire_notes_fichier(nom_fichier)

    if not state or state == -1:
        return (val, False)

    passed_students = [(k, i) for k, i in val.items() if i >= 10]

    return (passed_students, True)


def ajouter_etudiant(nom_fichier, nom, note):
    result, state = lire_notes_fichier(nom_fichier)

    if not state:
        sys.exit(result)

    if nom in result:
        return False

    try:
        with open(nom_fichier, "a") as f:
            f.write(nom + ";" + note)
            return True
    except FileNotFoundError:
        return (f"Error: File name '{nom_fichier}' does not exist.", False)


if len(sys.argv) < 2:
    sys.exit(
        "Usage: python3 main.py <action or help> <file name> <student name> <student note>"
    )


match sys.argv[1]:
    case "help":
        print("Usage: python3 main.py <action or help> <file name> <student name>")
        print()
        print("<actions> in English  | Frensh:")
        print("             avg      | moyenne")
        print("             best     | meilleure")
        print("             admitted | admis")
        print("             help")

    case "avg" | "moyenne":
        result, state = moyenne_classe(sys.argv[2])

        if not state:
            sys.exit(result)

        print(f"La moyenne de class est: {result}")

    case "best" | "meilleure":
        result, note, state = meilleure_note(sys.argv[2])

        if not state:
            sys.exit(result)

        print("--- Les etudiants ayant la meilleure note sont ---")

        for i, name in enumerate(result, start=1):
            print(f"{i}. {name.capitalize()}")

        print(f"Note: {note}")

    case "admitted" | "admis":
        result, state = admis(sys.argv[2])

        if not state:
            sys.exit(result)

        # print the students with there notes.
        print("--- Les etudiants admis (note >= 10) ---")
        for name, note in result:
            print(f"{name.capitalize()} : {note}")

    case "add" | "ajouter":
        state = ajouter_etudiant(sys.argv[2], sys.argv[3], sys.argv[4])

        if not state:
            sys.exit(f"Error: L'etudiant '{sys.argv[3]}' existent deja.")
        elif state:
            sys.exit("Etudiant ajouté avec succès.")
        else:
            sys.exit("Error: Unexpected return value.")

    case _:
        print("For help use the following command: python3 main.py help")
