##### Tri par selection
```algorithm
Algorithm   Tri_Par_Selection

Procedure Tri_Selection(T: tableau d'entier,n: entier)

Variables
    i, j, temp : entier

Debut
    Pour i <- 1 a n - 1 Faire
        Pour j <- i + 1 a n Faire
            si T[j] < T[i] Alors
                temp <- T[i]
                T[i] <- T[j]
                T[j] <- T[i]
            FinSi
        FinPour
    FinPour
FinProcedure

```
##### Tri a bulle
```algorithm
Algorithm   Tri_A_Bulle

Procedure Tri_Bulle(T: tableau d'Entier,N: Entier)

Variables
    temp, i, tn : entier
    echange : booleen
    
Debut
    
    tn <- N
    
    Faire
        echange <- Faux
        Pour i <- 1 a tn - 1 Faire
            Si T[i] > T[i + 1] Alors
                temp <- T[i]
                T[i] <- T[i + 1]
                T[i + 1] <- temp
                echange <- Vrai
            FinSi
        FinPour
        
        tn <- tn - 1
    TanQue(echange)
    
FinProcedure
```
