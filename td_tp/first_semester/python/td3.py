# ### Auteur : MOHAMED BOUHARTI
# ## TD 3

# ## Uncomment specific exercise


print("-----------------------------------")

# print("\n------Exercice ??------\n")
# if num < 10:
#     uniter = num
#     print(f"Unite : {num}")
# elif num < 100:
#     dizaine = num // 10
#     uniter = num % 10
#     print(f"dizaine: {dizaine}, Unite : {uniter}")
# elif num < 1000:
#     cenain = num // 100
#     dizaine = (num // 10) % 10
#     uniter = num % 10
#     print(f"cenain : {cenain}, dizaine: {dizaine}, uniter: {uniter}")
# else:
#     print("Invalid number!")

# print("\n------Exercice 1------\n")

# nbr = int(input("Enter a number: "))
# k = 1
# while k<=nbr:
#     print(k)
#     k+=1

# print("\n------Exercice 2------\n")

# A = 0
# B = int(input("Enter B:"))
# C = int(input("Enter C:"))

# if B == C:
#     A+=1

# while C>=0:
#     C = int(input("Enter C:"))
#     if B == C:
#         A+=1
# print("A = ",A)

# print("\n------Exercice 3------\n")

# i=0
# g_num = int(input("Entre un nomber: "))
# n=i+1
# i+=1

# while i<6:
#     num = int(input("Entre un nomber: "))

#     if num > g_num:
#         g_num = num
#         n=i+1

#     i+=1

# print("Grand nomber est: ",g_num)
# print("Sa position est: ",n)

# import math

# print("\n------Exercice 4------\n")

# nbr = int(input("Entre un nomber: "))
# S=1
# i=2
# # while i < math.sqrt(nbr):
# while (i*i) <= nbr:

#     if (nbr%i)==0:
#         S+=i
#         if (nbr//i)!=i:
#             S+=nbr//i
    
#     i+=1
# print(S)
# if S==nbr and nbr!=1:
#     print("'",nbr,"' est parfait.")
# else :
#     print("'",nbr,"' n'est pas parfait.")

# print("\n------Exercice 4------\n")

# num = int(input("Entre une nomber: "))

# som = 0

# for i in range(1,num):

#     if num%i==0:
#         som+=i
    
# if som==num:
#     print(f"Le nomber '{num}' est parfait.")
# else:
#     print(f"Le nomber '{num}' n'est pas parfait.")


# print("\n------Exercice 5------\n")

# num = int(input("Entre un nomber: "))

# while num<10 or num>20:

#     if num<10:
#         print("Plus Petit!")
#     if num>20:
#         print("Plus Grand!")

#     num = int(input("Entre un nomber: "))


# print("\n------Exercice 6------\n")
# num = int(input("Entre une nomber: "))

# stop = num+10
# #while num < stop:
# #    num += 1
# #    print(num)

# for i in range(0,10):
#    num += 1
#    print(num)

# print("\n------Exercice 7------\n")

# num=int(input("Entre un nomber: "))
# g_num=num
# i=0
# n=i+1
# i+=1

# while num!=0:
#     num=int(input("Entre un nomber: "))
#     if num>g_num:
#         g_num=num
#         n=i+1
#     i+=1

# print("Grand nomber: ",g_num)
# print("Position: ",n)

# print("\n------Exercice 8------\n")

# n = 0
# ch = str(input("Entre un nomber ([non] ou [Non] pour sortie): "))

# while ch != "non" and ch != "Non":
#     n += 1
#     ch = str(input("Entre un nomber ([non] ou [Non] pour sortie): "))
    
# print("Le nomber de valeurs saisire est :",n)

# print("\n------Exercice 9------\n")

# n = 0
# p = 0
# imp = 0

# nbr = int(input("Entre un nomber n (n<0 pour sortie): "))

# while nbr >= 0:
#     n+=1
#     if nbr%2 ==0:
#         p+=1
#     else:
#         imp+=1

#     nbr = int(input("Entre un nomber n (n<0 pour sortie): "))
    
# print("pair: ",p)
# print("impair: ",imp)
# print("total numbers: ",n)

# print("\n------Exercice 10------\n")

# c=input("Entre une charactaire: ")

# ch=str("")

# while c!='.':
    
#     if c == '0':
#         ch+=' '
#     else:
#         ch+=str(c)
    
#     c=input("Entre une charactaire: ")
    
# print(ch)

# print("\n------Exercice 9------\n")

# pair=0
# impair=0
# counter=0

# while True:

#     num = int(input("Etre un nomber:"))
    
#     if num<0:
#         break
    
#     counter+=1

#     if num %2==0:
#         pair+=1
#     else:
#         impair+=1



# print("Nombre de pairs :", pair)
# print("Nombre d'impairs :", impair)
# print("Total :", counter)

# print("\n------Exercice 10------\n")

# phrase=str("")

# while True:
    
#     ch=input("Entre une caractere: ")
    
#     if ch==".":
#         break
#     elif ch=="0":
#         phrase+=" "
#     else:
#         phrase+=ch

# print(f"phrase: {phrase}")
