//lesson 3
#include "http.h"

char *http_to_str(http_error_code_t code) {
  switch (code) {
    case 400:
      return "400 Bad Request";
    case 401:
      return "401 Unauthorized";
    case 404:
      return "404 Not Found";
    case 418:
      return "418 I AM A TEAPOT!";
    case 500:
      return "500 Internal Server Error";
    default:
      return "Unknown HTTP status code";
}
}

//lesson 4
#include <stdio.h>

typedef enum {
  BIG = 123412341234,
  BIGGER,
  BIGGEST,
} BigNumbers;

typedef enum {
  HTTP_BAD_REQUEST = 400,
  HTTP_UNAUTHORIZED = 401,
  HTTP_NOT_FOUND = 404,
  HTTP_I_AM_A_TEAPOT = 418,
  HTTP_INTERNAL_SERVER_ERROR = 500
} HttpErrorCode;

int main() {
  printf("The size of BigNumbers is %zu bytes\n", sizeof(BigNumbers));
  printf("The size of HttpErrorCode is %zu bytes\n", sizeof(HttpErrorCode));
  return 0;
}
