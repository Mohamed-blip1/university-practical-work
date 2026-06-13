#include <stdbool.h>
#include <stdio.h>

void printarr(int *arr, size_t size);

void echange(int *a, int *b);
void triSelection(int T[], size_t n);
void ex_1(int *T, size_t n);

void triBulle(int T[], size_t n);
void ex_2(int *T, size_t n);

int rechercheSequentielle(int T[], size_t n, int val);
void ex_3(int *T, size_t n);

int main()
{
  int T[10] = {2, 5, 23, 45, 56, 3, 12, 3, 25, 6};
  size_t n = 10;

  /* ex_1(T,n); */
  /* ex_2(T, n); */
  /* ex_3(T, n); */

  return 0;
}

void printarr(int *arr, size_t size)
{
  size_t i;

  for (i = 0; i < size; i++)
  {
    printf("arr[%zu] = %d\n", i, arr[i]);
  }
}

void echange(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

void triSelection(int T[], size_t n)
{
  size_t i, j;

  for (i = 0; i < n - 1; i++)
  {
    for (j = i + 1; j < n; j++)
    {
      if (T[i] > T[j])
      {
        echange(&T[i], &T[j]);
      }
    }
  }
}

void ex_1(int *T, size_t n)
{

  printf("---- ex_1 ----\n");

  printf("=== Before ===\n");
  printarr(T, n);

  triSelection(T, n);

  printf("=== After ===\n");
  printarr(T, n);
}

void triBulle(int T[], size_t n)
{
  size_t i;
  bool changed;

  do
  {
    changed = false;
    for (i = 0; i < n - 1; i++)
    {
      if (T[i] > T[i + 1])
      {
        echange(&T[i], &T[i + 1]);
        changed = true;
      }
    }
  } while (changed);
}

void ex_2(int *T, size_t n)
{
  printf("---- ex_2 ----\n");

  printf("=== Before ===\n");
  printarr(T, n);

  triBulle(T, n);

  printf("=== After ===\n");
  printarr(T, n);
}

int rechercheSequentielle(int T[], size_t n, int val)
{
  size_t i;

  for (i = 0; i < n; i++)
  {
    if (T[i] == val)
    {
      return (int)i;
    }
  }

  return -1;
}

int rechercheDichotomique(int T[], size_t n, int val)
{
  size_t left = 0, mid, right = n - 1;

  while (left <= right)
  {
    mid = (right + left) / 2;

#ifdef DEBUG
    printf("T[%zu] = %d\n", mid, T[mid]);
#endif

    if (T[mid] == val)
    {
      return (int)mid;
    }

    else if (T[mid] > val)
    {
      right = mid - 1;
    }
    else
    {
      left = mid + 1;
    }
  }

  return -1;
}

void ex_3(int *T, size_t n)
{
  int result, val;

  printf("---- ex_3 ----\n");

  printarr(T, n);

  printf("---- rechercheSequentielle ----\n");

  printf("Entre la Valeur a recherche: ");
  scanf("%d", &val);

  result = rechercheSequentielle(T, n, val);

  if (result == -1)
  {
    printf("'%d' n'exist pas dans le tableau.\n", val);
  }
  else
  {
    printf("'%d' exist dans la position: %d.\n", val, result);
  }

  triBulle(T, n);
  printarr(T, n);

  printf("---- rechercheDichotomique ----\n");

  printf("Entre la Valeur a recherche: ");
  scanf("%d", &val);

  result = rechercheDichotomique(T, n, val);

  if (result == -1)
  {
    printf("'%d' n'exist pas dans le tableau.\n", val);
  }
  else
  {
    printf("'%d' exist dans la position: %d.\n", val, result);
  }
}
