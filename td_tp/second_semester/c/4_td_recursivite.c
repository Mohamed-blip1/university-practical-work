#include <stdio.h>

float ex1(int *arr, int size);

int factorial(int n);

int fib_rec(int n);
int fib_it(int n);

int main(void)
{
  int arr[5] = {1, 1, 1, 1, 1};

  // printf("%.2f\n",  ex1(arr, 5));

  // printf("%d\n",factorial(3));

  printf("%d\n", fib_it(2));

  return 0;
}

float ex1(int *arr, int size)
{
  size -= 1;
  if (size < 0)
  {
    return 0;
  }
  if (size == 0)
  {
    return arr[0];
  }
  return arr[size] + ex1(arr, size);
}
int factorial(int n)
{
  if (n == 1 || n == 0)
  {
    return 1;
  }

  return n * factorial(n - 1);
}

int fib_rec(int n)
{
  if (n == 0)
  {
    return 0;
  }
  if (n == 1)
  {
    return 1;
  }

  return fib_rec(n - 1) + fib_rec(n - 2);
}

int fib_it(int n)
{
  if (n < 2)
  {
    return n;
  }

  int a = 0;
  int b = 1;

  int result = 0;

  for (int i = 2; i <= n; i++)
  {
    result = a + b;

    a = b;
    b = result;
  }

  return result;
}
