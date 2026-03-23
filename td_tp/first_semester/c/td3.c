/*
Auteur : MOHAMED BOUHARTI
TD 3

Uncomment specific exercise
*/

#include <stdio.h>

int main()
{
    // printf("\n------Exercice 1------\n");
    // int k = 1;
    // int nbr;

    // printf("Entre un nombner: ");
    // scanf("%d", &nbr);

    // while(k<=nbr)
    // {
    //     printf("%d\n",k);
    //     k+=1;
    // }
    // do
    // {
    //     printf("%d\n", k);
    //     k += 1;
    // } while (k <= nbr);

    // printf("\n------Exercice 2------\n");
    // int A = 0;
    // int B = 0;
    // int C = 0;

    // printf("Entre B: ");
    // scanf("%d", &B);
    // printf("Entre C: ");
    // scanf("%d", &C);

    // if (B == C)
    // {
    //     A += 1;
    // }

    // while (C >= 0)
    // {
    //     printf("Entre C: ");
    //     scanf("%d", &C);

    //     if (B == C)
    //     {
    //         A += 1;
    //     }
    // }

    // printf("Entre A = %d ",A);

    // printf("\n------Exercice 3------\n");

    // int i = 0;
    // int n = 0;
    // int num = 0;
    // int g_num = 0;

    // printf("Entre le nomber numero %d:", i + 1);
    // scanf("%d", &g_num);
    // n = i + 1;
    // i+=1;

    // do
    // {
    //     printf("Entre le nomber numero %d:", i + 1);
    //     scanf("%d", &num);

    //     if (num > g_num)
    //     {
    //         g_num = num;
    //         n = i + 1;
    //     }

    //     i += 1;
    // } while (i < 6);

    // printf("Grand nomber: %d\n",g_num);
    // printf("Sont position: %d\n",n);

    // printf("\n------Exercice 4------\n");

    // int nbr = 0;

    // printf("Entre un nomber (entier): ");
    // scanf("%d", &nbr);

    // int S = 0;
    // for (int i = 1; i * i <= nbr; ++i)
    // {
    //     if ((nbr % i) == 0)
    //     {
    //         S += i;

    //         if (((nbr / i) != i)&&(nbr / i)!=nbr && i != nbr)
    //         {
    //             S += (nbr / i);
    //         }
    //     }
    // }

    // if (S == nbr)
    // {
    //     printf("%d est parfait.\n", nbr);
    // }
    // else
    // {
    //     printf("%d n'est pas parfait.\n", nbr);
    // }

    // printf("\n------Exercice 5------\n");

    // int num = 0;

    // do
    // {
    //     printf("Entre un nomber: ");
    //     scanf("%d", &num);

    //     if (num < 10)
    //     {
    //         printf("Plus petit!\n");
    //     }
    //     if (num > 20)
    //     {
    //         printf("Plus Grand!\n");
    //     }

    // } while (num < 10 || num > 20);

    // printf("\n------Exercice 6------\n");

    // int num = 0;

    // printf("Entre un nomber: ");
    // scanf("%d", &num);

    // int stop = num + 10;

    // // while (num < stop)
    // // {
    // //     num+=1;
    // //     printf("%d\n",num);
    // // }

    // for (int i = 0; i < 10; i++)
    // {
    //     num+=1;
    //     printf("%d\n",num);
    // }

    // printf("\n------Exercice 7------\n");

    // int i=0;
    // int g_num=0;
    // printf("Entre un nomber ([0] pour sortie) %d :",i+1);
    // scanf("%d",&g_num);
    // int n=i+1;
    // i+=1;

    // int num;
    // do{
    //     printf("Entre un nomber ([0] pour sortie) %d :",i+1);
    //     scanf("%d",&num);
    //     if(num>g_num){
    //         g_num=num;
    //         n=i+1;
    //     }
    //     i+=1;
    // }while(num!=0);

    // printf("Grand nomber: %d\n",g_num);
    // printf("Sont position: %d\n",n);

    // #include <string.h>

    //     printf("\n------Exercice 8------\n");

    //     int n = 0;
    //     char ch[10];

    //     printf("Entre un nomber ([non] ou [Non] pour sortie): ");
    //     scanf("%9s", ch);

    //     while (strcmp(ch, "non") != 0 && strcmp(ch, "Non") != 0)
    //     {
    //         printf("ch = %s\n",ch);
    //         n += 1;
    //         int c;
    //         while((c=getchar()!='\n')&&c!=EOF);

    //         printf("Entre un nomber ([non] ou [Non] pour sortie): ");
    //         scanf("%9s", ch);
    //     }

    //     printf("Le nomber de valeurs sasis est: %d\n", n);

    // printf("\n------Exercice 9------\n");

    // int num = 0;
    // int p = 0;
    // int imp = 0;
    // int n;

    // do
    // {
    //     printf("Entre un nomber ([0] pour sortie): ");
    //     scanf("%d", &num);

    //     if (num != 0)
    //     {
    //         if (num % 2 == 0)
    //         {
    //             p += 1;
    //         }
    //         else if (num % 2 != 0)
    //         {
    //             imp += 1;
    //         }
    //         n += 1;
    //     }

    // } while (num != 0);

    // printf("Pair: %d\n",p);
    // printf("Impair: %d\n",imp);
    // printf("nomber: %d\n",n);

    // #include <string.h>

    //     printf("\n------Exercice 10------\n");

    // char ch[100];
    // int i = 0;
    // // char c[2];
    // char c1;

    // do
    // {
    //     printf("ch = %s\n", ch);

    //     printf("Entre une charactaire: ");
    //     scanf(" %c", &c1);

    //     if (c1 != '\n')
    //     {
    //         if (c1 == '0')
    //         {
    //             strcat(ch, " ");
    //         }
    //         else
    //         {
    //             ch[i] = c1;
    //         }
    //         i++;
    //     }

    //     // Method 2
    //     // printf("Entre une charactaire: ");
    //     // scanf("%1s", c);
    //     // if (c[0] == '0')
    //     // {
    //     //     strcat(ch, " ");
    //     // }
    //     // else
    //     // {
    //     //     strcat(ch, c);
    //     // }
    // } while (i < 100);

    return 0;
}
