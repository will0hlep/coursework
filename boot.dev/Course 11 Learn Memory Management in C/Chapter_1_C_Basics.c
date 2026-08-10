//lesson 1
#include <stdio.h>

int main() {
  printf("Starting the Sneklang interpreter...\n");
  return 0;
}

//lesson 2
#include <stdio.h>

int main() {
    printf("Program in C!\n");
    return 0;
}

//lesson 4
#include <stdio.h>

int main() {
  printf("starting sneklang tools\n");
  //does_not_exist("uh oh");
  printf("finished sneklang tools\n");
  return 0;
}

//lesson 5
#include <stdio.h>

int main() {
  /*
    Sneklang is for nvim enjoyers
    who want to write their own garbage
    collectors instead of using off-the-shelf
    solutions
  */
  printf("i use sneklang btw\n");
  printf("i use nvim btw\n");
  printf("i use arch btw\n");
  return 0;
}

//lesson 6
#include <stdio.h>

int main() {
  int max_recursive_calls = 100;
  char io_mode = 'w';
  float throttle_speed = 0.2;

  // don't touch below this line
  printf("Max recursive calls: %d\n", max_recursive_calls);
  printf("IO mode: %c\n", io_mode);
  printf("Throttle speed: %f\n", throttle_speed);
  return 0;
}

//lesson 7
#include <stdio.h>

int main() {
  char *will_never_hear_again =
      "Hey TJ, when is the memory course in C gonna be done?";

  // don't touch below this line
  printf("%s\n", will_never_hear_again);
  return 0;
}

//lesson 8
#include <stdio.h>

int main() {
  int sneklang_default_max_threads = 8;
  char sneklang_default_perms = 'r';
  float sneklang_default_pi = 3.141592;
  char *sneklang_title = "Sneklang";
  // don't touch above this line

  printf("Default max threads: %d\n",
         sneklang_default_max_threads);

  printf("Custom perms: %c\n",
         sneklang_default_perms);

  printf("Constant pi value: %f\n",
         sneklang_default_pi);

  printf("Sneklang title: %s\n",
         sneklang_title);

  return 0;
}

//lesson 10
#include <stdio.h>

int main() {
  int sneklang_int_size = 64;
  int sneklang_int_size = 32;
  printf("Sneklang int size: %d bits\n", sneklang_int_size);
  return 0;
}

//lesson 12
#include <stdio.h>

int max_sneklang_memory(int max_threads, int memory_per_thread) {
  return (int)(max_threads * memory_per_thread);
}

// don't touch below this line

void init_sneklang(int max_threads, int memory_per_thread) {
  printf("Initializing Sneklang\n");
  printf("Max threads: %d\n", max_threads);
  printf("Memory per thread: %d\n", memory_per_thread);
  int max_memory = max_sneklang_memory(max_threads, memory_per_thread);
  printf("Max memory: %d\n", max_memory);
  printf("====================================\n");
}

int main() {
  init_sneklang(4, 512);
  init_sneklang(8, 1024);
  init_sneklang(16, 2048);
  return 0;
}

//lesson 14
#include "exercise.h"

float get_average(int x, int y, int z) {
    return (x + y + z) / 3.0;
}

//lesson 15
float snek_score(int num_files, int num_contributors, int num_commits,
                 float avg_bug_criticality) {
  int size_factor = num_files * num_commits;
  int complexity_factor = size_factor + num_contributors;
  return complexity_factor * avg_bug_criticality;
}

//lesson 16
#include "exercise.h"

float celsius_is_better(int fahrenheit) {
  return (fahrenheit - 32) / 1.8;
}

char *get_temperature_status(int fahrenheit) {
  float celsius = celsius_is_better(fahrenheit);
  if (celsius > celsius_is_better(90)) {
      return "too hot";
  } else if (celsius < celsius_is_better(70)) {
      return "too cold";
  } else {
      return "just right";
  }
}

//lesson 17
#include "exercise.h"

int can_access_registry(int is_premium, int reputation, int has_2fa){
  if (is_premium || reputation >= 100 && has_2fa) {
    return 1;
  } else {
    return 0;
  }
}

//lesson 20
#include <stdbool.h>
#include <stdio.h>

int main() {
  // Use %zu is for printing `sizeof` result
  printf("sizeof(char)   = %zu\n", sizeof(char));
  printf("sizeof(bool)   = %zu\n", sizeof(bool));
  printf("sizeof(int)   = %zu\n", sizeof(int));
  printf("sizeof(float)   = %zu\n", sizeof(float));
  printf("sizeof(double)   = %zu\n", sizeof(double));
  printf("sizeof(size_t)   = %zu\n", sizeof(size_t));
}

//lesson 21
#include <stdio.h>

void print_numbers(int start, int end) {
  for (int i = start; i <= end; i++) {
    printf("%d\n", i);
  }
}

//lesson 22
#include <stdio.h>

void print_numbers_reverse(int start, int end) {
  int i = start;
  while (i >= end) {
    printf("%d\n", i);
    i--;
  }
}

//lesson 23
#include <stdio.h>

void print_numbers_reverse(int start, int end) {
  do {
    printf("%d\n", start);
    start--;
  } while (start >= end);
}