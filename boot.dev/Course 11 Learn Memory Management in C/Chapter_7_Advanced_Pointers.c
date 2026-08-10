//lesson 1
#include "exercise.h"
#include "stdlib.h"

void allocate_int(int **pointer_pointer, int value) {
  int *heap_int = malloc(sizeof(int));
  *pointer_pointer = heap_int;
  *heap_int = value;
}

//lesson 2
#include "exercise.h"
#include <stdlib.h>

token_t **create_token_pointer_array(token_t *tokens, size_t count) {
  token_t **token_pointers = malloc(count * sizeof(token_t *));
  if (token_pointers == NULL) {
    exit(1);
  }
  for (size_t i = 0; i < count; ++i) {
    token_t *heap_address = malloc(sizeof(token_t));
    token_pointers[i] = heap_address;
    *token_pointers[i] = tokens[i];
  }
  return token_pointers;
}

//lesson 3
#include "exercise.h"

void snek_zero_out(void *ptr, snek_object_kind_t kind) {
    if (kind == INTEGER) {
    ((snek_int_t*)ptr)->value = (int)0;
  } else if (kind == FLOAT) {
    ((snek_float_t*)ptr)->value = (float)0;
  } else {
    ((snek_bool_t*)ptr)->value = (unsigned int)0;
  }
}

//lesson 4
void swap_ints(int *a, int *b) {
  int temp_val = *a;
  *a = *b;
  *b = temp_val;
}

//lesson 5
void swap_strings(char **a, char **b) {
  char *temp_val = *a;
  *a = *b;
  *b = temp_val;
}

//lesson 6
#include <stdlib.h>
#include <string.h>

void swap(void *vp1, void *vp2, size_t size) {
  void *temp_val = malloc(size);
  memcpy(temp_val, vp1, size);
  memcpy(vp1, vp2, size);
  memcpy(vp2, temp_val, size);
  free(temp_val);
}
