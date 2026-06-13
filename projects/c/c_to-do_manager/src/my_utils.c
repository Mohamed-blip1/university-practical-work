// my_utils.c

#include "my_utils.h"

#include <ctype.h>  // isspace
#include <errno.h>  // ERANG
#include <limits.h> // INT_MAX, INT_MIN
#include <stdio.h>  // getchar, fgets, stdin, size_t
#include <stdlib.h> //
#include <string.h> // strcspn

UTILS_STATUS read_line(char *str, size_t size)
{
  int c;
  size_t len;

  if (str == NULL || size < 2)
  {
    return UTIL_FAIL;
  }

  if (!fgets(str, size, stdin))
  {
    return UTIL_FAIL;
  }

  len = strcspn(str, "\n");

  if (str[len] != '\n')
  {
    while ((c = getchar()) != '\n' && c != EOF)
      ;
    return UTIL_TRUNC;
  }

  str[len] = '\0';

  // Success no truncate
  return UTIL_SUCC;
}

UTILS_STATUS read_int(int *digit)
{
  char buffer[1024];
  char *endptr;
  long val;

  UTILS_STATUS status;

  if (digit == NULL)
  {
    return UTIL_FAIL;
  }

  status = read_line(buffer, sizeof(buffer));

  if (status != UTIL_SUCC)
  {
    return status;
  }

  errno = 0;
  val = strtol(buffer, &endptr, 10);

  while (isspace((unsigned char)*endptr))
  {
    endptr++;
  }

  if (endptr == buffer)
  {
    return UTIL_N_DIGIT;
  }
  else if (errno == ERANGE || val > INT_MAX || val < INT_MIN)
  {
    return UTIL_RANGE;
  }
  else if (*endptr != '\0')
  {
    return UTIL_N_DIGIT;
  }

  *digit = (int)val;

  return UTIL_SUCC;
}
