#lesson 1
def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage/5
    return total_damage, average_damage

#lesson 5
def update_player_score(current_score, increment):
    current_score += increment
    return current_score

#lesson 6
def get_hurt(current_health, damage):
    current_health -= damage
    return current_health

#lesson 7
def max_players_on_server():
    return 1.024e18, 1.024e19, 1.024e20

#lesson 13
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def get_create_bits(user_permissions):
    return user_permissions & can_create_guild

def get_review_bits(user_permissions):
    return user_permissions & can_review_guild

def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild

def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

#lesson 14
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    check = glorfindel | galadriel | elendil | elrond
    return check

def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)

# Don't edit below this line

def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")

main()

#lesson 16
def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers = int(num_servers,2)
    num_players = int(num_players,2)
    num_admins = int(num_admins,2)
    return num_servers, num_players, num_admins