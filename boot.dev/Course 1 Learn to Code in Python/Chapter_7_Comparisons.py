#lesson 1
def player_1_wins(player_1_score, player_2_score):
    return player_1_score>player_2_score

#lesson 2
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height==edward_height
    is_alphonse_edward_same = alphonse_height==edward_height
    is_winry_alphonse_same = winry_height==alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

#lesson 3
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage

#lesson 4
def print_status(player_health):
    if player_health <= 0:
        print('dead')
    print('status check complete')

# Don't edit below this line

def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")

def main():
    test(0)
    test(5)
    test(-1)
    test(3)

main()

#lesson 5
def check_swords_for_army(number_of_swords, number_of_soldiers):
    sword_message = 'correct amount'
    if number_of_swords != number_of_soldiers:
        sword_message = 'in' + sword_message
    return sword_message

#lesson 6
def player_status(health):
    if health > 5:
        return 'healthy'
    elif health > 0:
        return 'injured'
    else:
        return 'dead'
    
#lesson 7
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
    
#lesson 8
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return 'high'
    elif player_name == low_scoring_player_name:
        return 'low'
    else:
        return 'neither'

#lesson 9
def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20

#lesson 11
def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21:
        if not on_break:
            if 5 <= time <= 10:
                return True
    return False

#lesson 12
def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"

#lesson 13
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False
    power_difference = player_power - enemy_defense
    if power_difference>0:
        advantage = True
    elif power_difference==0:
        evenly_matched = True
    else:
        disadvantage = True
    return advantage, disadvantage, evenly_matched