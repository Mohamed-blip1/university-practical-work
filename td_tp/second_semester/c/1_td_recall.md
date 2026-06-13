#### Exercise 3
  * A
  ```algorithm
Algorithm   montant_a_payer

Variables
    montant, remise : reel

Debut
    Ecrire "Entre le montant: "
    Lire(montant)
    
    si montant > 30 Alors
        remise <- montant * (2 * (1/100))
        montant <- montant - remise
    Fin si
    
    Ecrire "Le montant a payer: ", montant, "MAD"
Fin
  ```
  * B
  ```algorithm
Algorithm impot

Variables
    age : entier
    sexe : caractere
    
Debut
    Ecrire "Entre l'age: "
    Lire(age)
    
    Ecrire "Entre l'sexe (F/M): "
    Lire(sexe)

    Si (sexe = 'M' alors et age > 20) OU (sexe = 'F' et age >= 18 et age <= 35 ) alors
        Ecrire "L'habitant est imposable."
    Sino
        Ecrire "L'habitant n'est pas imposable."
    Fin si
Fin
  ```

#### Exercise 4
```algorithm
Algorithm   dimension_d'un_tableau

Variables
    tableau T[50]                                   : entier
    i, j, n, somme, valeur_max, valeur_max_position : entier
    
Debut

    Fair 
        Ecrire "Entre la dimension (1-50): "
        Lire(n)
    TanQue(n < 1 OU n > 50)
    
    Pour i <- 1 a n Fair
        Ecrire "T[", i, "] = "
        Lire(T[i])
    FinPour
    
    // Somme
    somme <- 0
    Pour i <- 1 a n Fair
        somme <- somme + T[i]
    FinPour
    Ecrire "La somme : ", somme
    
    // Effecer les 0 et Tasser
    j <- 0
    Pour i <- 1 a n Fair
        Si T[i] != 0 Alors
            j <- j + 1
            T[j] <- T[i]
        FinSi
    FinPour
    n <- j
    
    Ecrire "Tableau apres tassement :"
    Pour i <- 1 a n Fair
        Ecrire "T[",i,"] = ", T[i]
    FinPour
    
    // Maximum et position
    valeur_max <- T[1]
    valeur_max_position <- 1
    Pour i <- 2 a n Fair
        Si T[i] > valeur_max Fair
            valeur_max <- T[i]
            valeur_max_position <- i
        FinSi
    FinPour
   
    Ecrire "La valeur maximale du tableau est: ", valeur_max
    Ecrire "Sa position est: ", valeur_max_position
    
Fin
```

#### Exercice 5
```algorithm
Algorithm   supprime_caractere

Variables
    str  : chain de caractere
    c    : caractere
    i, j : entier
    
Debut
    Ecrire "Entre une chain de caractere: "
    Lire(str)
    
    Ecrire "Entre une caractere: "
    Lire(c)
    
    j <- 1
    Pour i <- 1 a n Fair
        Si str[i] <> c Alors
            str[j] <- str[i]
            j <- j + 1
        FinSi
    FinPour
    
    str[j] <- "\0"
    
    Ecrire "Resultat: ", str
```

#### Exercice 6
```algorithm
Algorithm   cercle

Fonction Surface(r: reel): reel
Debut
    Retourner 3.14 * (r^2)
Fin Fonction

Fonction Perimetre(r: reel): reel
Debut
    Retourner 2 * 3.14 * r
Fin Fonction

Variables
    r, srf, prt : reel
    
Debut
    Ecrire "Entre le rayon: "
    Lire(r)
    
    srf <- Surface(r)
    prt <- Perimetre(r)
    
    Ecrire "La surface = ", srf
    Ecrire "Le perimetre = ", prt
Fin
```

#### Exercice 7
```algorithm
Algorithm ..

Fonction Valurs_Egal(A: tableau entier,B: tableau  entier, N: entier): entier

Variables
    i, conteur: entier
    
Debut
    conteur <- 0
    
    Pour i <- 1 a N Fair
        Si A[i] = B[i] Alors
            conteur <- conteur + 1
        Fin Si
    Fin Pour
    
    Retourner conteur
    
Fin Fonction
        
```

#### Exercice 8
```algorithm
Algorithm   copie_valeurs_negative

Fonction cvn(T: tableau reel, TNEG: tableau reel, N: entier): entier

Variables
    i, n_TNEG : entier

Debut
    
    n_TNEG <- 1
    
    Pour i <- 1 a N Fair
        Si T[i] < 0 Alors
            TNEG[n_TNEG] <- T[i]
            n_TNEG <- n_TNEG + 1
        Fin Si
    Fin Pour
    
    Retourner n_TNEG - 1
FinFonction
```
