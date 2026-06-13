#### Exercice 1

```algorithm
Algorithm   distance_entre_points

Type Structure Point
    x: reel
    y: reel
FinStruct

Variables
    a, b: Point
    distance, dx, dy: reel

Debut
    Ecrire "Entre les coordonnees de a:"
    Ecrire "x: "
    Lire(a.x)
    Ecrire "y: "
    Lire(a.y)
    
    Ecrire "Entre les coordonnees de b:"
    Ecrire "x: "
    Lire(b.x)
    Ecrire "y: "
    Lire(b.y)
    
    dx <- b.x - a.x
    dy <- b.y - a.y
    
    distance <- sqrt(dx^2 + dy^2)
    
    Ecrire "La distance est: ", distance
Fin
```

#### Exercice 2
```algorithm
Algorithm   Etudiants

Type Structure Etudiant
    nom     : chain
    prenom  : chain
    note    : reel
FinStruct

Variables
    tableau E[100] : Etudiant
    i, n : entier

Debut
    Ecrire "Entre nombre d'etudiants: "
    Lire(n)
    
    Si n > 100 alors
        n <- 100
    FinSi
    
    Pour i <- 1 a n Faire
        Ecrire "--- Etudiant ", i, "/", n, "---"
        
        Ecrire "nom: "
        Lire(E[i].nom)
        
        Ecrire "prenom: "
        Lire(E[i].prenom)
    
        Faire
            Ecrire "note (0-20): "
            Lire(E[i].note)
            
            Si NON (E[i].note>=0 ET E[i].note<=20) Alors
                Ecrire "Error: La note doit etre entre 0 et 20."
            FinSi
        TanQue(NON (E[i].note>=0 ET E[i].note<=20))
        
        Ecrire ""
    FinPour
    
    Ecrire "List d'etudiant ayant une note >= 10/20"
    Ecrire "---------------------------------------"
    
    Pour i <- 1 a n Faire
        Si E[i].note >= 10 Alors
            Ecrire "- ", E[i].nom, " ", E[i].prenom, "(note: ", E[i].note, ")"
        FinSi
    FinPour
Fin 
```
