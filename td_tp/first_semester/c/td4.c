/*
Auteur : MOHAMED BOUHARTI
TD 4

Uncomment specific exercise
*/

#include <stdio.h>
#include <stdbool.h>

int main()
{

    printf("\n--------exercice 1--------\n");

    // float T[20];

    // for(int i=0;i<20;i++){
    //     printf("Entre un nomber: ");
    //     scanf("%f",&T[i]);
    // }

    // float some =0;

    // for(int i=0;i<20;i++){
    //     some += T[i];
    // }

    // printf("Some: %f",some);

    // printf("\n--------exercice 2--------\n");

    // int len=30;

    // // scanf("%d", &len);

    // int T[len];

    // for (int i = 0; i < len; i++)
    // {
    //     printf("Entre un nomber: ");
    //     scanf("%d", &T[i]);
    // }

    // int petit = T[0];
    // int pos = 0;
    // for (int i = 1; i < len; i++)
    // {
    //     if (petit > T[i])
    //     {
    //         petit = T[i];
    //         pos = i;
    //     }
    // }

    // printf("le petit elem est: %d\n", petit);
    // printf("sont positin est: %d\n", pos + 1);

    // printf("\n--------exercice 3--------\n");

    // char C[10];
    // char c;
    // for (int i = 0; i < 10; i++)
    // {
    //     printf("Entre une caracter: ");
    //     scanf(" %c", &C[i]);
    // }

    // printf("\nC:\n");
    // int n_m_lettre = 0;
    // int n_lettre = 0;
    // for (int i = 0; i < 10; i++)
    // {
    //     printf("%c", C[i]);
    //     if (C[i] >= 'A' && C[i] <= 'Z')
    //     {
    //         n_m_lettre += 1;
    //         n_lettre += 1;
    //     }
    //     else if (C[i] >= 'a' && C[i] <= 'z')
    //     {
    //         n_lettre += 1;
    //     }
    // }

    // printf("letter number: %d\n",n_lettre);
    // printf("majuscule letters nomber: %d\n",n_m_lettre);

    // printf("\n--------exercice 4--------\n");

    // int len = 40;

    // int N[len];

    // printf("Entre la note d'eleve: \n");
    // for (int i = 0; i < len; i++)
    // {
    //     printf("Nomber %d : ", i);
    //     scanf("%d", &N[i]);
    // }

    // int moyenne = 0;
    // int max = N[0];

    // for (int i = 0; i < len; i++)
    // {

    //     moyenne += N[i];
    //     if (N[i] > max)
    //     {
    //         max = N[i];
    //     }

    //     // printf("%d : %d\n",i,N[i]);
    // }

    // moyenne /= len;

    // int n_moyenne = 0;
    // int n_max = 0;

    // for (int i = 0; i < len; i++)
    // {

    //     if (N[i] > moyenne)
    //     {
    //         n_moyenne += 1;
    //     }
    //     if (N[i] == max)
    //     {
    //         n_max += 1;
    //     }
    // }

    // // Debug
    // // printf("moyenne: %d\n",moyenne);

    // printf("le nombre des notes supérieures strictement à la moyenne est: %d\n", n_moyenne);
    // printf("le nombre d'occurrence de la note maximale est: %d\n", n_max);

    // printf("\n--------exercice 5--------\n");

    // int len = 10;
    // int T[len];

    // for (int i = 0; i < len; i++)
    // {
    //     printf("Entre un nomber: ");
    //     scanf("%d", &T[i]);
    // }
    // int min = T[0];
    // int max = T[5];

    // // int i = 1;
    // // int j = len - 1;

    // // while (i < j)
    // // {
    // //     if (min > T[i])
    // //     {
    // //         min = T[i];
    // //     }

    // //     if (max < T[j])
    // //     {
    // //         max = T[j];
    // //     }

    // //     i++;
    // //     j--;
    // // }

    // for (int i = 0; i < 5; i++)
    // {
    //     if (min > T[i])
    //     {
    //         min = T[i];
    //     }

    //     if (max < T[i+5])
    //     {
    //         max = T[i+5];
    //     }
    // }

    // printf("le minimum de la 1ère moitié: %d\n", min);
    // printf("le maximum de la 2ère moitié: %d\n", max);

    //     printf("\n--------exercice 6--------\n");
    // #include <stdbool.h>

    //     int len;
    //     printf("Entre le range de Tableau: ");
    //     scanf("%d", &len);

    //     int T[len];

    //     for (int i = 0; i < len; i++)
    //     {
    //         printf("entre un nomber: ");
    //         scanf("%d", &T[i]);
    //     }

    //     int x;

    //     printf("Entre le nomber en cherche: ");
    //     scanf("%d", &x);

    //     bool exist = false;

    //     for (int i = 0; i < len; i++)
    //     {
    //         if (T[i] == x)
    //         {
    //             exist = true;
    //             break;
    //         }
    //     }

    //     if (exist == true)
    //     {
    //         printf("'%d' exist.\n", x);
    //     }
    //     else
    //     {
    //         printf("'%d' n'exist pas!\n", x);
    //     }

    // printf("\n--------exercice 7--------\n");

    // int len;
    // printf("Entre le range des tableaus: ");
    // scanf("%d", &len);

    // int U[len];
    // int V[len];

    // printf("Entre l'element de tableau U:\n");
    // for (int i = 0; i < len; i++)
    // {

    //     printf("Entre un nomber: ");
    //     scanf("%d", &U[i]);
    // }

    // printf("Entre l'element de tableau V:\n");
    // for (int i = 0; i < len; i++)
    // {

    //     printf("Entre un nomber: ");
    //     scanf("%d", &V[i]);
    // }

    // /* Debug:
    // printf("V: ");
    // for (int i = 0; i < len; i++)
    // {
    //     printf("%d - ", U[i]);
    // }
    // printf("\nU: ");
    // for (int i = 0; i < len; i++)
    // {
    //     printf("%d - ", V[i]);
    // }*/

    // int P[len * len][2]; // produit cartésien
    // int S[len];          // Some

    // int p_scalaire=0; // produit scalaire

    // for (int i = 0; i < len; i++)
    // {
    //     S[i] = U[i] + V[i];
    //     p_scalaire += U[i] * V[i];
    // }

    // int p = 0;
    // for (int i = 0; i < len; i++)
    // {
    //     int first = U[i];

    //     for (int j = 0; j < len; j++)
    //     {
    //         P[p][0] = first;
    //         P[p][1] = V[j];
    //         p++;
    //     }
    // }

    // /* Debug:
    //     for (int i = 0; i < len * len; i++)
    //     {

    //         printf("%d: %d\n", P[i][0], P[i][1]);
    //     }
    //     */

    // printf("\n--------exercice 8--------\n");

    // int len;

    // printf("Entre le range de tableau: ");
    // scanf("%d", &len);

    // int T[len];

    // for (int i = 0; i < len; i++)
    // {
    //     printf("Entre un nombre: ");
    //     scanf("%d", &T[i]);
    // }

    // printf("T: ");
    // for (int i = 0; i < len; i++)
    // {
    //     printf("%d-", T[i]);
    // }

    // int i = 0;
    // int j = len - 1;
    // while (i < j)
    // {
    //     int temp = T[i];
    //     T[i] = T[j];
    //     T[j] = temp;

    //     i++;
    //     j--;
    // }

    // printf("\nT: ");
    // for (int i = 0; i < len; i++)
    // {
    //     printf("%d-", T[i]);
    // }

    // printf("\n--------exercice 9--------\n");

    // int line = 5;
    // int colonne = 5;
    // int T[line][colonne];

    // printf("Entre le element :\n");
    // for (int i = 0; i < line; i++)
    // {

    //     printf("De line %d:\n", i + 1);

    //     for (int j = 0; j < colonne; j++)
    //     {

    //         printf("Entre un nomber :");
    //         scanf("%d", &T[i][j]);
    //     }
    // }

    // int some = 0;
    // int count_pos = 0;
    // int some_pos = 0;
    // int some_neg = 0;
    // int max = T[0][0];
    // int min = T[0][0];
    // int mx_pos_i = 0;
    // int mx_pos_j = 0;
    // int mn_pos_i = 0;
    // int mn_pos_j = 0;

    // for (int i = 0; i < line; i++)
    // {
    //     for (int j = 0; j < colonne; j++)
    //     {
    //         int num = T[i][j];
    //         some += num;

    //         if (num > 0)
    //         {
    //             count_pos += 1;
    //             some_pos += num;
    //         }
    //         else if (num < 0)
    //         {
    //             some_neg += num;
    //         }
    //         if (num > max)
    //         {
    //             max = num;
    //             mx_pos_i = i;
    //             mx_pos_j = j;
    //         }
    //         if (num < min)
    //         {
    //             min = num;
    //             mn_pos_i = i;
    //             mn_pos_j = j;
    //         }
    //     }
    // }

    return 0;
}
