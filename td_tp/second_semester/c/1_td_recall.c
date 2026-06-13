#define _USE_MATH_DEFINES_
#include <math.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define BUFFER_SIZE 512
#define ARR_CAPACITY 10

void ex_1();
void ex_2();
void ex_3_a();
void ex_3_b();
void ex_4_b();
void ex_5();
float ex_6_area(float r);          // A = Pi * r^2
float ex_6_circumference(float r); // C = 2r * Pi
int ex_7(int *arr_1, int *arr_2, size_t arr_1_size, size_t arr_2_size);
void test_ex_7();
int ex_8(const int *T, int *TNEG, size_t T_size, size_t *TNEG_size,
         size_t TNEG_capacity);
void test_ex_8();

int main()
{
  srand(time(NULL));

  // ex_1();
  // ex_2(); // Sum of digits of a number
  // ex_3_a();
  // ex_3_b();
  // ex_4_b();
  /* ex_5(); */
  /* printf("area of a r = 5 circle: %.2f\n", ex_6_area(5)); */
  /* printf("circumference of a r = 5 circle: %.2f\n", ex_6_circumference(5));*/
  /* test_ex_7(); */
  /* test_ex_8(); */

  return 0;
}

void ex_1()
{
  int a = 20;
  int b = 5;
  int c = -10;
  int d = 2;
  int x = 12;
  int y = 15;

  int result_1 = (5 * x) + 2 * ((3 * b) + 4);
  printf("1 = %d\n", result_1); // Should give: 98

  int result_2 = (5 * (x + 2) * 3) * (b + 4);
  printf("2 = %d\n", result_2); // Should give: 1890

  int result_3 = (a == (b = 5));
  printf("3 = %d\n", result_3); // Should give: 0

  int result_4 = (a += (x + 5));
  printf("4 = %d\n", result_4); // Should give: 37

  // a = 37

  int result_5 = (a != (c *= (-d)));
  printf("5 = %d\n", result_5); // Should give: 1

  /* printf("a = %d\n", a); */
  // c = 20

  // 37 *= -20 + (12 - 2)
  int result_6 = (a *= (c + (x - d)));
  printf("6 = %d\n", result_6); // Should give: 37 * 30 = 1110

  int result_7 = (a %= d++);
  printf("7 = %d\n", result_7); // Should give 0

  int result_8 = (a %= --d);
  printf("8 = %d\n", result_8); // Should give 0

  // a = 0

  int result_9 = (x++) * (a + c);
  printf("9 = %d\n", result_9); // Should give 240

  // x = 13

  // a = (13 * (1) + 15 * 0) = 13
  int result_10 = (a = (x * (b < c) + y * !(b < c)));
  printf("10 = %d\n", result_10); // Should give 13
}

void ex_2()
{
  // Sum of digits of a number

  int n;
  int number;
  int somme;

  printf("Enter a integer: ");
  scanf("%d", &n);
  somme = 0;

  while (n != 0)
  {
    number = n % 10;
    somme = somme + number;
    n = n / 10;
  }

  printf("Result: %d\n", somme);
}

void ex_3_a()
{
  float amount;
  float discount = 0.02;

  printf("Enter the initial amount in MAD: ");
  scanf("%f", &amount);

  if (amount > 30)
  {
    amount -= amount * discount;
  }

  printf("Amount to pay is: %.2f MAD\n", amount);
}

void ex_3_b()
{
  char sex;
  int age;

  printf("Enter your age: ");
  scanf("%d", &age);

  printf("Enter your sex: ");
  scanf(" %c", &sex);

  if (((sex == 'M' || sex == 'm') && age > 20) ||
      ((sex == 'F' || sex == 'f') && age >= 18 && age <= 35))
  {
    printf("The resident is subject to tax.\n");
  }
  else
  {
    printf("The resident is not subject to tax.\n");
  }
}

void ex_4_b()
{
  int T[50];
  int d, i, j, sum, max, max_p;

  // 1.
  do
  {
    printf("Enter the dimension (1-50): ");
    scanf("%d", &d);
  } while (d < 1 || d > 50);

  for (i = 0; i < d; i++)
  {
    printf("T[%d] = ", i);
    scanf("%d", &T[i]);
  }

  // 2.
  sum = 0;
  for (i = 0; i < d; i++)
  {
    sum += T[i];
  }
  printf("sum : %d\n", sum);

  // 3.
  j = 0;
  for (i = 0; i < d; i++)
  {
    if (T[i] != 0)
    {
      T[j] = T[i];
      j++;
    }
  }
  d = j;

  // 4.
  for (i = 0; i < d; i++)
  {
    printf("T[%d] : %d\n", i, T[i]);
  }

  // 5.
  if (d > 0)
  {
    max = T[0];
    max_p = 0;
    for (i = 1; i < d; i++)
    {
      if (T[i] > max)
      {
        max = T[i];
        max_p = i;
      }
    }
    printf("Max: %d, in position: %d\n", max, max_p);
  }
  else
  {
    printf("The table is empty after removing all zeros.\n");
  }
}

void ex_5()
{
  char buffer[BUFFER_SIZE];
  char target;
  int i, j;

  printf("Enter a string: ");
  // scanf("%511s", buffer);
  fgets(buffer, BUFFER_SIZE, stdin);
  size_t len = strcspn(buffer, "\n");
  buffer[len] = '\0';

  printf("Enter the target character: ");
  scanf(" %c", &target);

#ifdef DEBUG
  printf("string size = %zu\n", strlen(buffer));
#endif

  printf("string = %s\n", buffer);
  printf("target = %c\n", target);

  j = 0;
  for (i = 0; buffer[i] != '\0'; i++)
  {
    if (buffer[i] != target)
    {
      buffer[j] = buffer[i];
      j++;
    }
  }
  buffer[j] = '\0';

#ifdef DEBUG
  printf("string size = %zu\n", strlen(buffer));
#endif

  printf("string = %s\n", buffer);
  printf("target = %c\n", target);
}

float ex_6_area(float r) { return M_PI * r * r; }
float ex_6_circumference(float r) { return M_PI * 2 * r; }

// -1 indicate an error
int ex_7(int *arr_1, int *arr_2, size_t arr_1_size, size_t arr_2_size)
{
  size_t i;
  int count = 0;

  if (arr_1_size != arr_2_size)
  {
    return -1;
  }

  for (i = 0; i < arr_1_size; i++)
  {
    if (arr_1[i] == arr_2[i])
    {
      count++;
    }
  }

  return count;
}

void test_ex_7()
{

  int arr1[ARR_CAPACITY];
  int arr2[ARR_CAPACITY];
  size_t i;
  int result;

  for (i = 0; i < ARR_CAPACITY; i++)
  {
    arr1[i] = rand() % 20 + 1;
    arr2[i] = rand() % 20 + 1;
  }

#ifdef DEBUG
  for (i = 0; i < ARR_CAPACITY; i++)
  {
    printf("arr1[%zu] = %d | ", i, arr1[i]);
  }
  printf("\n");
  for (i = 0; i < ARR_CAPACITY; i++)
  {
    printf("arr2[%zu] = %d | ", i, arr2[i]);
  }
  printf("\n");
#endif

  result = ex_7(arr1, arr2, ARR_CAPACITY, ARR_CAPACITY);

  if (result == -1)
  {
    printf("Error: arr1 and arr2 does not have the same size.\n");
  }
  else
  {
    printf("arr1 and arr2 have %d same elements.\n", result);
  }
}

// This function overwrite TNEG
int ex_8(const int *T, int *TNEG, size_t T_size, size_t *TNEG_size,
         size_t TNEG_capacity)
{
  size_t i;
  *TNEG_size = 0;

  if (T == NULL || TNEG == NULL)
  {
    // NULL pointer
    return -1;
  }

  for (i = 0; i < T_size; i++)
  {
    if (T[i] < 0)
    {
      if (*TNEG_size >= TNEG_capacity)
      {
        // NO SPACE
        return -2;
      }

      TNEG[*TNEG_size] = T[i];
      (*TNEG_size)++;
    }
  }

  return *TNEG_size;
}

void test_ex_8()
{
  int T[ARR_CAPACITY] = {-3, -2, -1, 0, 1, 2, 3, -100};
  int TNEG[ARR_CAPACITY];
  size_t T_size = 8;
  size_t TNEG_size = 0;

  size_t i;

  ex_8(T, TNEG, T_size, &TNEG_size, ARR_CAPACITY);

  for (i = 0; i < T_size; i++)
  {
    printf("T[%zu] = %d | ", i, T[i]);
  }
  printf("\n");
  for (i = 0; i < TNEG_size; i++)
  {
    printf("TNEG[%zu] = %d | ", i, TNEG[i]);
  }
  printf("\n");
}
