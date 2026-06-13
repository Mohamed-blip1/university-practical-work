#include <stdio.h>

#define MAX_CHR 64

typedef struct
{
  char name[MAX_CHR];
  int age;
  char email[MAX_CHR];

} Person;

int add_persons(char *file_name, int num);
int print_persons(char *file_name);

int main(void)
{
  int n;
  char *file_name = "persons.txr";

  printf("Enter how many porsons (n): ");
  scanf("%d", &n);

  if (n <= 0)
  {
    printf("Error: n <= 0.\n");
    return 1;
  }

  if (add_persons(file_name, n) == 0)
  {
    return 1;
  }
  if (print_persons(file_name) == 0)
  {
    return 1;
  }

  return 0;
}

int add_persons(char *file_name, int num)
{
  Person P;
  if (num <= 0)
    return 0;

  FILE *f = fopen(file_name, "a");

  if (!f)
    return 0;

  for (int i = 0; i < num; i++)
  {
    printf("Person %d :\n", i + 1);
    printf("nom: ");
    scanf("%63s", P.name);
    printf("age: ");
    scanf("%d", &P.age);
    printf("email: ");
    scanf("%63s", P.email);
    printf("\n");

    fprintf(f, "%s %d %s\n", P.name, P.age, P.email);
  }

  fclose(f);
  return 1;
}

int print_persons(char *file_name)
{
  Person P;

  FILE *f = fopen(file_name, "r");

  if (!f)
  {
    return 0;
  }

  int i = 1;

  printf("\n--- Persons ---\n");

  while (fscanf(f, "%s %d %s", P.name, &P.age, P.email) != EOF)
  {
    printf("[%d] Nom: %s | Age: %d | Email: %s\n", i++, P.name, P.age, P.email);
  }

  fclose(f);
  return 1;
}
