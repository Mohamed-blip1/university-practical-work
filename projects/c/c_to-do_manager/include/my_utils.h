#ifndef MY_UTILS_H
#define MY_UTILS_H

// utils.h

#include <stdio.h>

typedef enum
{
  UTIL_FAIL,
  UTIL_SUCC,
  UTIL_TRUNC,
  UTIL_N_SPACE,
  UTIL_N_DIGIT,
  UTIL_RANGE,
} UTILS_STATUS;

UTILS_STATUS read_line(char str[], size_t maxlen);
UTILS_STATUS read_int(int *digit);

#endif
