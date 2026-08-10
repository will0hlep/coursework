//lesson 1
#include "snekstack.h"
#include <stdlib.h>

stack_t *stack_new(size_t capacity) {
  stack_t *Stack = malloc(sizeof(stack_t));
  if (Stack == NULL) {
    return NULL;
  }
  Stack->count = 0;
  Stack->capacity = capacity;
  Stack->data = malloc(capacity * sizeof(void *));
  if ((Stack->data) == NULL) {
    free(Stack);
    return NULL;
  }
  return Stack;
}

//lesson 2
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **new_data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack == NULL) {
      stack->capacity /= 2;
      return;
    }
    stack->data = new_data;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

// don't touch below this line

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

//lesson 3
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }
  return stack->data[--stack->count];
}

// don't touch below this line'

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;

      exit(1);
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

//lesson 4
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }
  free(stack->data);
  free(stack);
}

// don't touch below this line

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;
      exit(1);
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

//lesson 5
#include "snekstack.h"
#include "stdlib.h"

void scary_double_push(stack_t *s) {
  stack_push(s, (void *)1337);
  int *new_int = malloc(sizeof(int));
  *new_int = 1024;
  stack_push(s, new_int);
}

//lesson 6
#include "snekstack.h"
#include "stdlib.h"
#include <string.h>

void stack_push_multiple_types(stack_t *s) {
  float *new_float = malloc(sizeof(float));
  *new_float = 3.14;
  stack_push(s, new_float);
  char *tmp_str = "Sneklang is blazingly slow!";
  char *new_str = malloc((strlen(tmp_str) + 1) * sizeof(char));
  memcpy(new_str, tmp_str, strlen(tmp_str) + 1);
  stack_push(s, new_str);
}