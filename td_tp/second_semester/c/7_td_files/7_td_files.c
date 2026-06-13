#include <stdbool.h>
#include <stdio.h>
#include <string.h>

void ex_1();
int ex_2();
void ex_3();
int add_persons(char *file_name, int num);
bool print_persons(char *file_name);

int main()
{
  /* ex_1(); */
  /* if (ex_2()) */
  /* { */
  /*   printf("1\n"); */
  /* } */
  /* else */
  /* { */

  /*   printf("-1\n"); */
  /* } */

  ex_3();

  return 0;
}

void Afficher(char *file_name)
{
  FILE *f = fopen(file_name, "r");
  int c;

  if (!f)
  {
    printf("Error: Cannot open the file '%s'.\n", file_name);
    return;
  }

  while (fscanf(f, "%d", &c) != EOF)
  {
    printf("%d\n", c);
  }

  fclose(f);
}

int nbr_caractere(char *file_name)
{
  FILE *f = fopen(file_name, "r");
  int count = 0;
  int c;

  if (!f)
  {
    printf("Error: Cannot open the file '%s'.\n", file_name);
    return -1;
  }

  while ((c = fgetc(f)) != EOF)
  {
    count += 1;
  }

  fclose(f);

  return count;
}

int nbr_lines(char *file_name)
{
  FILE *f = fopen(file_name, "r");

  int count = 0;
  int c;
  int last_c;

  if (!f)
  {
    printf("Error: Cannot open the file '%s'.\n", file_name);
    return -1;
  }

  while ((c = fgetc(f)) != EOF)
  {

    if (c == '\n')
    {
      count += 1;
    }
    last_c = c;
  }

  if (last_c != '\n')
  {
    count += 1;
  }

  fclose(f);

  printf("Number of lines in '%s' file is: %d\n", file_name, count);

  return count;
}

void Copie(char *file_name)
{
  char *des_file = "numbers2.txt";

  FILE *f = fopen(file_name, "r");
  FILE *des_f = fopen(des_file, "w");

  int c;

  if (!f || !des_f)
  {
    printf("Error: Cannot open the file '%s'.\n", file_name);
    return;
  }

  while ((c = fgetc(f)) != EOF)
  {
    fputc(c, des_f);
  }

  printf("'%s' Copied to '%s'\n", file_name, des_file);

  fclose(f);
  fclose(des_f);
}

void ex_1()
{
  char *file_name = "numbers.txt";
  int result;

  Afficher(file_name);

  result = nbr_caractere(file_name);
  if (result == -1)
    printf("Error: nbr_caractere().\n");
  else
    printf("Number of caracters in '%s' file is: %d\n", file_name, result);

  result = nbr_lines(file_name);
  if (result == -1)
    printf("Error: nbr_lines().\n");

  Copie(file_name);
}

int ex_2()
{
  int x;
  char file_name[24] = "tableX.txt";
  char c;

  printf("Enter X: ");
  scanf("%d", &x);

  c = x + '0';
  file_name[5] = c;
  FILE *f = fopen(file_name, "w");

  if (!f)
    return 0;

  for (int i = 1; i <= 10; i++)
  {
    fprintf(f, "%dx%d=%d\n", x, i, x * i);
  }

  fclose(f);
  return 1;
}

typedef struct
{
  char name[64];
  int age;
  char email[64];
} Person;

int add_persons(char *file_name, int num)
{
  FILE *f = fopen(file_name, "a");

  char name[64];
  int age;
  char email[64];

  if (f == NULL)
  {
    return false;
  }

  Person p;

  for (int i = 0; i < num; i++)
  {
    printf("Entre person '%d':\n", i + 1);

    printf("name: ");
    scanf("%63s", p.name);

    printf("age: ");
    scanf("%d", &p.age);

    printf("email: ");
    scanf("%63s", p.email);

    fprintf(f, "%s %d %s\n", p.name, p.age, p.email);
  }

  fclose(f);

  return true;
}

bool print_persons(char *file_name)
{

  FILE *f = fopen(file_name, "r");

  char name[64];
  int age;
  char email[64];

  Person p;

  if (!f)
  {
    return false;
  }

  printf("--- Personnes ---\n");
  int i = 1;
  while (fscanf(f, "%63s %d %63s", p.name, &p.age, p.email) == 3)
  {

    printf("[%d] Name: %s | Age: %d | Email: %s\n", i++, p.name, p.age,
           p.email);
    printf("\n");
  }
  return true;
}

void ex_3()
{
  char *file_name = "prsons.txt";
  add_persons(file_name, 3);

  print_persons(file_name);
}
