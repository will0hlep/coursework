//lesson 1
#pragma once

struct Coordinate {
  int x; int y; int z;
};

//lesson 3
#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};

struct Coordinate new_coord(int x, int y, int z);
struct Coordinate scale_coordinate(struct Coordinate coord, int factor);

//lesson 4
#pragma once

typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

coordinate_t new_coord(int x, int y, int z);
coordinate_t scale_coordinate(coordinate_t coord, int factor);

//lesson 6
#pragma once

typedef struct SneklangVar {
  double weight;
  int scope_level;
  int value;
  char *name;
  char type;
  char is_constant;
} sneklang_var_t;
