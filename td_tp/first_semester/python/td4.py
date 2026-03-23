# ### Auteur : MOHAMED BOUHARTI
# ## TD 4

# ## Uncomment specific exercise


print("-----------------------------------")

# print("--------Exercice 1--------")

# T=[]

# for i in range(0,5):
#     T.append(float(input(f"Entre le nomber numero {i+1}: ")))

# some=0
# for i in T:
#     some+=i

# print(f"T = {T}")

# print(f"Some = {some}")


# print("--------Exercice 2--------")

# T=[]

# for i in range(0,5):
#     T.append(int(input("Entre un nomber: ")))

# petit=T[0]
# pos=0
# for i in range(1,len(T)):
#     if T[i]<petit:
#         petit=T[i]
#         pos = i

# print(f"petit = {petit}")
# print(f"position est : {pos+1}")

# print("--------Exercice 3--------")

# T=[]

# for _ in range(0,10):

#     temp = input("Entre une caractere: ")

#     if len(temp)!=1:
#         T.append((""))
#     # if not temp:
#     #     T.append((""))
#     else:
#         T.append((temp[0]))
#     print(T)

# n_m_letter=0
# n_letter=0


# for i in range(0,10):
#     if T[i]>='A' and T[i]<='Z':
#         n_m_letter+=1
#         n_letter+=1
#     elif T[i]>='a' and T[i]<='z':
#         n_letter+=1

# print(f"number of letters est :{n_letter}")
# print(f"number of majuscules letters est :{n_m_letter}")

# print("--------Exercice 4--------")

# T=[]

# print("entre a note de l'eleve: ")
# for i in range(0,5):
#     T.append(int(input(f"Nomber {i} : ")))

# moyenne=0
# max=T[0]
# for i in T:
#     moyenne += i
#     if max<i:
#         max=i

# moyenne=moyenne/len(T)
# n_moyenne=0
# n_max=0

# for i in T:
#     if i > moyenne :
#         n_moyenne+=1
#     if max==i:
#         n_max+=1

# # print(f"moyenne = {moyenne}")
# # print(f"max = {max}")

# print(f"nomber supérieures strictement de la moyenne : {n_moyenne}")
# print(f"nomber d'occurrence de la note maximale : {n_max}")

# print("--------Exercice 5--------")

# T=[]

# for i in range(0,10):
#     T.append(int(input("Entre un nomber: ")))

# min=T[0]
# max=T[5]

# for i in range(0,5):
#     if min > T[i]:
#         min=T[i]
#     if max < T[i+5]:
#         max=T[i+5]

# print(f"le minimum de la 1ère moitié: {min}")
# print(f"le maximum de la 2ère moitié: {max}")

# print("--------Exercice 6--------")

# len=int(input("Donne la range de tableau: "))

# T=[]

# for i in range(0,len):
#     T.append(int(input("Entre un nomber: ")))

# exist=False

# x=int(input("Donne le nombre a chercher: "))

# for i in range(0,len):
#     if x==T[i]:
#         exist=True

# if exist==True:
#     print(f"'{x}' exist.")
# else:
#     print(f"'{x}' n'exist pas!")

# print("--------Exercice 7--------")

# N=int(input("Entre le range des tableau: "))

# U = []
# V = []

# print("Entre l'elements de U:")
# for i in range(0,N):
#     U.append(int(input("Entre un nomber: ")))

# print("Entre l'elements de V:")
# for i in range(0,N):
#     V.append(int(input("Entre un nomber: ")))

# P=[]
# S=[]
# p_scal=0

# for i in range(0,N):
#     S.append(U[i]+V[i])
#     p_scal+=U[i]*V[i]

# for i in range(0,N):
#     termp=U[i]
#     for j in range(0,N):
#         temp=[]
#         temp.append(U[i])
#         temp.append(V[j])
#         P.append(temp)

# print(P)

# print("--------Exercice 8--------")

# len=int(input("Entre le range de tableau: "))

# T=[]

# for i in range(0,len):
#     T.append(int(input("Entre un nomber: ")))

# i=0
# j=len-1

# print(T)
# while i<j:
#     temp=T[i]
#     T[i]=T[j]
#     T[j]=temp

#     i+=1
#     j-=1
# print(T)

# print("--------Exercice 9--------")

# line=int(input("Entre le nomber des lines: "))
# colonne=int(input("Entre le nomber des colonne: "))

# M=[]

# for i in range(0,line):
#     temp=[]

#     print(f"Entre l'elements de line {i+1}: ")
#     for _ in range(0,colonne):
#         temp.append(int(input("Entre un nomber: ")))

#     M.append(temp)

# print(M)

# some=0
# counter_pos=0
# SomP=0
# SomN=0
# max=M[0][0]
# min=M[0][0]
# l_max=0
# c_max=0
# l_min=0
# c_min=0


# for i in range(0,line):

#     for j in range(0,colonne):
#         num=M[i][j]
#         some+=num
        
#         if num>0:
#             counter_pos+=1
#             SomP+=num
#         elif num<0:
#             SomN+=num
        
#         if max<num:
#             max=num
#             l_max=i
        #     c_max=j

        # if min>num: # <= can it be elif ? No.
        #     min=num
        #     l_min=i
        #     c_min=j

