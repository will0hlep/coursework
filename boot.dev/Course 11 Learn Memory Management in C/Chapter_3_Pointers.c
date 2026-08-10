//lesson 1
#include "snek.h"

unsigned long size_of_addr(long long i) {
  unsigned long sizeof_snek_version = sizeof(i);
  return sizeof(&sizeof_snek_version);
}

//lesson 5
#include "coordinate.h"

void coordinate_update_x(coordinate_t coord, int new_x) {
  coord.x = new_x;
}

coordinate_t coordinate_update_and_return_x(coordinate_t coord, int new_x) {
  coord.x = new_x;
  return coord;
}

//lesson 6
#include "exercise.h"

codefile_t change_filetype(codefile_t *f, int new_filetype) {
  codefile_t new_f = *f;
  new_f.filetype = new_filetype
  return new_f;
}

//lesson 8
#include "exercise.h"

void update_file(int filedata[200], int new_filetype, int new_num_lines) {
  filedata[1] = new_num_lines;
  filedata[2] = new_filetype;
  filedata[199] = 0;
}

//lesson 11
#include "exercise.h"
#include <stdio.h>

void dump_graphics(graphics_t gsettings[10]) {
  int *ptr = (int *)gsettings;
  for (int i = 0; i < 30; i++) {
    printf("settings[%d] = %d\n", i, ptr[i]);
  }
}

//lesson 13
#include <stdio.h>

void core_utils_func(int core_utilization[]) {
  printf("sizeof core_utilization in core_utils_func: %d\n", sizeof(core_utilization));
}

// don't touch below this line

int main() {
  int core_utilization[] = {43, 67, 89, 92, 71, 43, 56, 12};
  int len = sizeof(core_utilization) / sizeof(core_utilization[0]);
  printf("sizeof core_utilization in main: %zu\n", sizeof(core_utilization));
  printf("len of core_utilization: %d\n", len);
  core_utils_func(core_utilization);
  return 0;
}

//lesson 14
#include "exercise.h"
#include <stdio.h>

void concat_strings(char *str1, const char *str2) {
  char *i = str1;
  while (*i != '\0') {
    i++;
  }
  char *j = str2;
  while (*j != '\0') {
    *i = *j;
    i++;
    j++;
  }

  *i = '\0';
}

//lesson 15
#include "exercise.h"
#include <string.h>

int smart_append(TextBuffer *dest, const char *src) {
  if (!dest || !src) {
    return 1;
  } else {
    int mbs = 64;
    int srclen = strlen(src);
    int remaining = mbs - dest->length - 1;
    if (srclen > remaining) {
      strncat(dest->buffer, src, remaining);
      dest->length = mbs - 1;
      return 1;
    } else {
        strcat(dest->buffer, src);
        dest->length += srclen;
        return 0;
    }
  }
}

//lesson 16
typedef struct SnekObject snekobject_t;

typedef struct SnekObject {
  char *name;
  snekobject_t *child;
} snekobject_t;

snekobject_t new_node(char *name);