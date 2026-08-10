//Challenge 1
#include <stdio.h>

int count_high_scores(const int scores[], int length, int min_score) {
  int count = 0;
  for (int i = 0; i < length; i++) {
    if (scores[i] >= min_score) {
      count++;
    }
  }
  return count;
}

//challenge 2
#include <stdlib.h>
#include "exercise.h"

void player_init(player_t *player, const char *name) {
  int i = 0;
  if (name != NULL) {
    while (name[i] != '\0' && i < 31) {
      player->name[i] = name[i];
      i++;
    }
  }
  player->name[i] = '\0';
  player->xp = 0;
  player->level = 1;
}

void gain_xp(player_t *player, int amount) {
  if (amount>0 && player != NULL) {
    player->xp += amount;
    while (player->xp>=100) {
      player->level ++;
      player->xp -= 100;
    }
  }
}

player_t *player_new(const char *name) {
  player_t *player = (player_t *)malloc(sizeof(player_t));
  if (player == NULL) {
    return NULL;
  }
  player_init(player, name);
  return player;
}

//challange 3
#include <stdlib.h>
#include <string.h>

char *path_join(const char *dir, const char *file) {
  size_t dir_len = strlen(dir);
  size_t file_len = strlen(file);

  if (dir_len==0 && file_len!=0) {
    char *inb = malloc(file_len + 1);
    strcpy(inb,file);
    return inb;
    
  } else if (dir_len!=0 && file_len==0) {
    char *ina = malloc(dir_len + 1);
    strcpy(ina,dir);
    return ina;
    
  } else if (dir_len!=0 && file_len!=0) {
    
    char *ina = malloc(dir_len + 1);
    strcpy(ina, dir);
    while (ina[dir_len-1] == '/') {
      ina[dir_len-1] = '\0';
      dir_len --;
    }
  
    int i = 0;
    while (file[i] == '/') {
      i ++;
    }
    char *inb = malloc(file_len + 1);
    strcpy(inb, file+i);
    
    char *out = malloc(dir_len + file_len + 2);
    if (!out) return NULL;
    strcpy(out, ina);
    strcat(out, "/");
    strcat(out, inb);
    free(ina);
    free(inb);
    return out;
  }
  return "";
}
