#lesson 1
def get_character_record(name, server, level, rank):
    return {'name' : name,
              'server' : server,
              'level' : level,
              'rank' : rank,
              'id' : name + '#' + server}

#lesson 2 
def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
    }
    
#lesson 7
def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy in enemy_names:
        if enemy not in enemies_dict:
            enemies_dict[enemy] = 1
        else:
            enemies_dict[enemy] += 1
    return enemies_dict

#lesson 8
def get_most_common_enemy(enemies_dict):
    most_common_enemy = None
    most_common_enemy_count = float('-inf')
    for enemy in enemies_dict:
        enemy_count = enemies_dict[enemy]
        if enemy_count > most_common_enemy_count:
            most_common_enemy_count = enemy_count
            most_common_enemy = enemy
    return most_common_enemy

#lesson 10
def get_quest_status(progress):
    return progress['quests']['bridge_run']['status']

#lesson 11
def merge(dict1, dict2):
    new_dict = {}
    for dictionary in [dict1, dict2]:
        for key in dictionary:
            new_dict[key] = dictionary[key]
    return new_dict