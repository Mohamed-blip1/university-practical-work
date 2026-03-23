# ### Auteur : MOHAMED BOUHARTI
# ## TD 1

# ## Uncomment specific exercise


print("-----------------------------------")

# # Exercice 2
# print("\n------Exercice 2------\n")

# A=3
# B=5
# A=B
# #C=a+b   # a et b ne s'ont pas declarees. "algorithm produit un Error"
# #C='9'   # '9' est de type caractere, alore aue C est de type reel 
# print("Reponce: algorithm produit un Error, pare ce que a et b ne s'ont pas declarees.")
# print("           Ensuite '9' est de type caractere, alore aue C est de type reel")

# #----------------------------------#
# print("\n------Exercice 3------\n")
# print("a)\n")

# A=5     # A = 5
# B=A+4   # B = A+4 = 9
# A=A+1   # A = 5+1 = 6
# B=A-4   # B = 6-4 = 2

# # Donc A = 6 et B = 2

# print("A =",A,",B =",B,"\n") # Aficher les valure des variable

# #-------------------
# print("b)\n")

# A=3     # A = 3
# B=10    # B = 10
# C=A+B   # C = 3+10 = 13
# A=C     # A = 13

# # Donc A = 13 et B = 10 et C = 13

# print("A =",A,",B =",B,",C =",C,"\n") # Aficher les valure des variable

# #-------------------
# print("c)\n")

# A=3     # A = 3
# B=10    # B = 10
# C=A+B   # C = 3+10 = 13
# A=C     # A = 13

# # Donc A = 13 et B = 10 et C = 13

# print("A =",A,",B =",B,",C =",C,"\n") # Aficher les valure des variable

# print("Reponce: les deux dernières instructions ne permettent-elles pas d'échanger les deux valeurs de B et A.")
# print("les deux A et B sera a la valure de B.\n")
# print("Reponce: Si l'on inverse les deux dernières instructions, cela ne changera rien du tout,")
# print(" hormis le fait que cettefois, c'est les deux A et B sera la valure de A\n")

# #----------------------------------#
# print("\n------Exercice 4------\n")

# A = "423"
# B = "12"
# C = A + B

# print("Reponce: l'algorithme, il sera un chaine de caractere C qui sera un valure combine de la valure de A et B qui est '42312' come un chaine de caractere")
# print("\nla valure de C =",C)

# #----------------------------------#
# print("\n------Exercice 5------\n")

# A=10
# B=20

# print("Avant : A =",A,",B =",B,"\n") # Aficher les valure des variable

# C=A
# A=B
# B=C

# print("Apres : A =",A,",B =",B,"\n") # Aficher les valure des variable

# #----------------------------------#
# print("\n------Exercice 6------\n")

# A=30
# B=60
# C=80

# print("Avant : A =",A,",B =",B,",C =",C,"\n") # Aficher les valure des variable

# D=B
# B=A # B = A

# E=C
# C=D # C = B 

# A=E # A = C

# # # ou
# # X=A
# # Y=B
# # Z=C
# # # apres
# # B = X
# # C = Y
# # A = Z

# print("Apres : A =",A,",B =",B,",C =",C,"\n") # Aficher les valure des variable

# #----------------------------------#
# print("\n------Exercice 7------\n")

# x=5
# y=12

# print("Les valuer avant : x =",x,",y =",y,"\n") # Aficher les valure des variable

# x = x + y
# y = x - y
# x = x - y

# print("Les valuer apres : x =",x,",y =",y,"\n") # Aficher les valure des variable

# print("Repons : En generale ce sequence des instruction qui nous permi de echanger les valure de deux entiere variables")

# #----------------------------------#
# print("\n------Exercice 8------\n")

# A = 30
# B = A * 2

# print("B =",B)

# C = (B+A)/4
# B = C/5

# D = "Amine"

# E = (A > 40) or (C < B)

# print("les valeurs obtenues sont : A = ", A , "B = ",B , " C = ", C , " D = ", D, "E = ", E)

# #----------------------------------#
# print("\n------Exercice 9------\n")

# print("Algorithm de calculation:\n")

# a=int(input("Entrer le premier valure : "))
# b=int(input("Entrer le premier valure : "))

# print("\n")
# print("La some           : ",a+b)
# print("La soustraction   : ",a-b)
# print("La division       : ",a/b)
# print("La multiplication : ",a*b)
# print("La modulo         : ",a%b)


# #----------------------------------#
# print("\n------Exercice 10------\n")

# print("Algorithm d'affiche la longueur d'un chaîne de caractères:\n")

# chain=str(input("Entrer un chaine de caracteres : "))

# print("\n")
# print("la longueur de '",chain,"' et  :", len(chain))

# #----------------------------------#
# print("\n------Exercice 11------\n")

# print("Algorithm de calcule et affiche la distance entre deux points A(x1,y1) et B(x2,y2) :\n")

# print("Entrer les valures de A:")
# x1=int(input("x1 : "))
# y1=int(input("y1 : "))
# print("Entrer les valures de B:")
# x2=int(input("x2 : "))
# y2=int(input("y2 : "))

# import math # pour le fonction sqrt()

# AB= math.sqrt((x2-x1)**2 + (y2-y1)**2)

# print("AB = ",AB)

# #----------------------------------#
# print("\n------Exercice 12------\n")

# print("Algorithm pour calcule pour chaque élève la moyenne des notes :\n")

# print("Entrer les note des matieres suivant:")

# Math=int(input("Math : "))
# Physique=int(input("Physique : "))
# Francer=int(input("Francer : "))
# Anglais=int(input("Anglais : "))
# Geographie=int(input("Geographie : "))

# moyenne= (Math*5 + Physique*5 +  Francer*4 + Anglais*2 +  Geographie*3)/(5+5+4+2+3)

# print("la moyenne :", moyenne)

#----------------------------------#
# print("\n------Exercice 13------\n")

# print("Algorithm de convertir un nombre de secondes en un nombre d'heures,de minutes et de secondes. :\n")

# input_secondes=int(input("Entrer un nombre de secondes : "))

# houres = input_secondes //3600
# minutes = input_secondes //60 %60
# second = input_secondes %60

# print(input_secondes,"s est equivalente a: ",houres,"h ",minutes,"min ",second,"s")
