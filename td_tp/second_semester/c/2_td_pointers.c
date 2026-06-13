#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define ARR_SIZE 10
#define BUFFER_SIZE 512

void ex_1();
void ex_2();
void ex_3();
void ex_4();
void ex_5();
void ex_6(int b, int n, int *res);
void test_ex_6();
void ex_7();

int main()
{
  srand(time(NULL));

  /* ex_1(); */
  ex_2();
  /* ex_3(); */
  /* ex_4(); */
  /* ex_5(); */
  /* test_ex_6(); */
  /* ex_7(); */

  return 0;
}

void ex_1()
{
  int i = 4;
  int j = 10;

  int *p;
  int *q;

  p = &i;
  q = &j;

  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 4, j = 10, p = 4, q = 10
  *p = *p + *q;
  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 14, j = 10, p = 14, q = 10
  p = &j;
  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 14, j = 10, p = 10, q = 10
  *q = *q + *p;
  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 14, j = 20, p = 20, q = 20
  q = &i;
  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 14, j = 20, p = 20, q = 14
  i = 4;
  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 4, j = 20, p = 20, q = 4
  *q = *q + 1;
  printf("i=%d, j=%d, p=%d, q=%d\n", i, j, *p,
         *q); // i = 5, j = 20, p = 20, q = 5
}

void ex_2()
{
  int A[] = {12, 23, 27, 42, 67, 70, 73, 76, 89, 90};
  int *p;
  p = A;
  printf("A: %d, B: %d, C: %d\n", *p + 2, *(p + 2),
         *(p + (*p - 9))); // A: 14, B: 27, C: 42
}

void ex_3()
{
  int A[ARR_SIZE];
  size_t A_size = ARR_SIZE;
  int X;
  size_t i;

  int *p1;
  int *p2;

  p1 = A;
  i = 0;
  while (p1 != &A[A_size])
  {
    printf("A[%zu] = ", i);
    scanf("%d", p1);
    i++;
    p1++;
  }

  printf("Enter a number to delete from the A:");
  scanf("%d", &X);

  printf("\n=== Old Arr ===\n");

  p1 = A;
  i = 0;
  while (p1 != &A[A_size])
  {
    printf("A[%zu] = %d\n", i, *p1);
    i++;
    p1++;
  }

  p1 = A;
  p2 = A;
  while (p1 != &A[A_size])
  {
    if (*p1 != X)
    {
      *p2 = *p1;
      p2++;
    }
    p1++;
  }

  // New A size
  A_size = p2 - A;

  printf("\n=== New Array ===\n");
  p1 = A;
  i = 0;
  while (p1 != &A[A_size])
  {
    printf("A[%zu] = %d\n", i, *p1);
    i++;
    p1++;
  }
}

void ex_4()
{
  int A[ARR_SIZE];
  size_t A_size = ARR_SIZE;
  int *p1, *p2;
  int AIDE;

  p1 = A;
  while (p1 < A + A_size)
  {
    *p1 = (int)(p1 - A);
    p1++;
  }

  printf("\n=== Old Array ===\n");
  p1 = A;
  while (p1 < A + A_size)
  {
    printf("A[%zu] = %d\n", (p1 - A), *p1);
    p1++;
  }

  p1 = A;
  p2 = A + A_size - 1;
  while (p1 < p2)
  {
    AIDE = *p1;
    *p1 = *p2;
    *p2 = AIDE;

    p1++;
    p2--;
  }

  printf("\n=== New Array ===\n");
  p1 = A;
  while (p1 < A + A_size)
  {
    printf("A[%zu] = %d\n", (p1 - A), *p1);
    p1++;
  }
}

void ex_5()
{
  char CH[BUFFER_SIZE];
  char *P;
  size_t CH_len;

  printf("Enter a string: ");
  fgets(CH, BUFFER_SIZE, stdin);
  CH[strcspn(CH, "\n")] = '\0';

  P = CH;
  while (*P != '\0')
  {
    P++;
  }
  CH_len = (P - CH);

  printf("len(CH) = %zu\n", CH_len);
}

void ex_6(int b, int n, int *res)
{
  int i;

  *res = b;
  for (i = 1; i < n; i++)
  {
    *res *= b;
  }
}

void test_ex_6()
{
  int res;
  int b = 2;
  int n = 3;

  ex_6(b, n, &res);

  printf("%d^%d = %d\n", b, n, res);
}

void ex_7()
{
  int *arr_p;
  size_t arr_size, i;

  printf("Enter a array size: ");
  scanf("%zu", &arr_size);

  arr_p = malloc(arr_size * sizeof(int));

  if (arr_p == NULL)
  {
    fprintf(stderr, "Memory allocation failed!\n");
    return;
  }

  for (i = 0; i < arr_size; i++)
  {
    arr_p[i] = i;
  }

  for (i = 0; i < arr_size; i++)
  {
    printf("arr[%zu] = %d\n", i, arr_p[i]);
  }

  free(arr_p);

  arr_p = NULL;
}
