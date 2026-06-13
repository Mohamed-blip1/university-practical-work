#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

void ex_1();
void ex_2();
void ex_3();
void ex_4();
void ex_5();

int main()
{
  /* ex_1(); */
  /* ex_2(); */
  /* ex_3(); */
  /* ex_4(); */
  ex_5();

  return 0;
}

void ex_1()
{
  typedef struct
  {
    float x;
    float y;
  } Point;

  Point a, b;
  float distance;

  printf("Entre le coordonnes du point a:\n");

  printf("x = ");
  scanf("%f", &a.x);
  printf("y = ");
  scanf("%f", &a.y);

  printf("Entre le coordonnes du point b:\n");

  printf("x = ");
  scanf("%f", &b.x);
  printf("y = ");
  scanf("%f", &b.y);

  float dx = (b.x - a.x);
  float dy = (b.y - a.y);

  distance = sqrt(dx * dx + dy * dy);

  printf("La distance entre a et b est: %.2f\n", distance);
}

void ex_2()
{
  typedef struct
  {
    char fname[52];
    char lname[52];
    float note;
  } Etudiant;

  Etudiant etudiants[100];
  int n;

  printf("Entre le nombre d'etudiants n: ");
  scanf("%d", &n);

  if (n > 100)
  {
    n = 100;
    printf("100 etudiant maximum.\n");
  }

  printf("\n");
  for (int i = 0; i < n; i++)
  {
    printf("--- Etudiant %d/%d ---\n", i + 1, n);
    printf("Prenom: ");
    scanf("%s", etudiants[i].fname);
    /* fgets(etudiants[i].fname, sizeof(etudiants[i].fname), stdin); */

    printf("nom: ");
    scanf("%s", etudiants[i].lname);
    /* fgets(etudiants[i].lname, sizeof(etudiants[i].fname), stdin); */

    do
    {
      printf("note (0-20): ");
      scanf("%f", &etudiants[i].note);

      if (!(etudiants[i].note >= 0 && etudiants[i].note <= 20))
      {
        printf("Error: La note doit être entre 0 et 20.\n");
      }
    } while (!(etudiants[i].note >= 0 && etudiants[i].note <= 20));

    printf("\n");
  }

  printf("List d'etudiants ayant un not >= 10/20:\n");

  printf("\n");
  for (int i = 0; i < n; i++)
  {
    if (etudiants[i].note >= 10)
    {
      printf("- %s %s (Note: %.2f)\n", etudiants[i].fname, etudiants[i].lname,
             etudiants[i].note);
    }
  }
}

void ex_3()
{
  typedef struct
  {
    char *name;
    int id;
  } Person;

  char buffer[BUFFER_SIZE];
  size_t i;
  int c;

  Person P[5];

  for (i = 0; i < 5; i++)
  {
    printf("--- Person %zu/5 ---\n", i + 1);

    printf("nom: ");
    fgets(buffer, sizeof(buffer), stdin);
    buffer[strcspn(buffer, "\n")] = '\0';

    /* printf("strlen(buffer): %zu\n", strlen(buffer)); */

    P[i].name = (char *)malloc(strlen(buffer) + 1);
    strcpy(P[i].name, buffer);

    /* printf("strlen(buffer): %zu\n", strlen(P.name)); */
    /* printf("person name is : %s\n", P.name); */

    printf("id: ");
    scanf("%d", &P[i].id);

    while ((c = getchar()) != '\n' && c != EOF)
      ;

    printf("\n");
  }

  for (i = 0; i < 5; i++)
  {
    printf("- nom: %s (id: %d)\n", P[i].name, P[i].id);
  }

  for (i = 0; i < 5; i++)
  {
    free(P[i].name);
    P[i].name = NULL;
  }
}

void terminate(char *s) { s[strcspn(s, "\n")] = '\0'; }
void p_l_m(char *s)
{
  if (s[0] >= 'a' && s[0] <= 'z')
  {
    s[0] -= ('a' - 'A');
  }
}

// TODO: refactor ex_4
void ex_4()
{
  typedef struct
  {
    char nom[24];
    char prenom[24];
  } Person;

  typedef struct
  {
    Person h;
    Person f;
  } Couple;

  Couple *couples;
  size_t i, n;
  int c;

  printf("Entre le nombre de couples: ");
  scanf("%zu", &n);

  while ((c = getchar()) != '\n' && c != EOF)
    ;

  couples = (Couple *)malloc(n * sizeof(Couple));

  for (i = 0; i < n; i++)
  {
    printf("--- Couple %zu/%zu ---\n\n", i + 1, n);

    printf("-- Homme --\n");
    printf("nom: ");
    fgets(couples[i].h.nom, sizeof(couples[i].h.nom), stdin);
    terminate(couples[i].h.nom);
    p_l_m(couples[i].h.nom);

    printf("prenom: ");
    fgets(couples[i].h.prenom, sizeof(couples[i].h.prenom), stdin);
    terminate(couples[i].h.prenom);
    p_l_m(couples[i].h.prenom);

    printf("\n");

    printf("-- femme --\n");
    printf("nom: ");
    fgets(couples[i].f.nom, sizeof(couples[i].f.nom), stdin);
    terminate(couples[i].f.nom);
    p_l_m(couples[i].f.nom);

    printf("prenom: ");
    fgets(couples[i].f.prenom, sizeof(couples[i].f.prenom), stdin);
    terminate(couples[i].f.prenom);
    p_l_m(couples[i].f.prenom);

    printf("\n");
  }

  for (i = 0; i < n; i++)
  {
    printf("Mr %s %s est le mari de Mme %s %s.\n", couples[i].h.prenom,
           couples[i].h.nom, couples[i].f.prenom, couples[i].f.nom);
  }

  free(couples);
  couples = NULL;
}

typedef struct
{
  char Nom[64];
  int Age;
  float Taille;
} Fonctionnaire;

Fonctionnaire compare_age(Fonctionnaire *P1, Fonctionnaire *P2)
{
  return (P1->Age >= P2->Age) ? *P1 : *P2;
}

float cal_moyenne(Fonctionnaire *P1, Fonctionnaire *P2)
{
  return (P1->Taille + P2->Taille) / 2;
}

void ex_5()
{
  Fonctionnaire P1 = {.Nom = "Ali", .Age = 20, .Taille = 160};
  Fonctionnaire P2 = {.Nom = "Omar", .Age = 21, .Taille = 170};

  Fonctionnaire P = compare_age(&P1, &P2);

  printf("Le persone le plus agee :\n");
  printf("Nom: %s, Age: %d, Taille: %.2f\n", P.Nom, P.Age, P.Taille);

  printf("Le moyenne de Taille de les deux persones est: %.2f\n",
         cal_moyenne(&P1, &P2));
}
