#lesson 1
def print_numbers():
    for i in range(100):
        print(i)

# Don't edit below this line

def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")

def main():
    test()

main()

#lesson 2
def print_numbers():
    for i in range(200):
        print(i)

# Don't edit below this line

def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")

def main():
    test()

main()

#lesson 3
def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)

# Don't edit below this line

def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")

def main():
    test(16)
    test(6)
    test(11)

main()

#lesson 7
def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

# Don't edit below this line

def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")

def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)

main()

#lesson 8
def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

#lesson 9
def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

#lesson 10
def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health

#lesson 11
def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter += 1
        if counter < 3:
            continue
        else:
            enchantment_strength = quest_number * 5
            print(
                f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
            )
            counter = 0

# Don't touch below this line

def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")

def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)

main()

#lesson 12
def check_defense(attack_strength, min_enchantment, max_enchantment):
    for enchantment_strength in range(min_enchantment, max_enchantment + 1):
        print(
            f"Comparing attack strength {attack_strength} to enchantment strength {enchantment_strength}."
        )

        if enchantment_strength >= attack_strength:
            print("Attack blocked!")
            break

# Don't touch below this line

def test(attack_strength, min_enchantment, max_enchantment):
    print(
        f"Testing attack strength {attack_strength} vs. enchantment strengths {min_enchantment}–{max_enchantment}:"
    )
    check_defense(attack_strength, min_enchantment, max_enchantment)
    print("========================================")

def main():
    test(5, 8, 12)
    test(8, 6, 10)
    test(10, 5, 8)
    test(7, 4, 7)

main()

#lesson 13
def countdown_to_start():
    for i in range(10,0,-1):
        string_to_print = f'{i}...'
        if i == 1:
            string_to_print += 'Fight!'
        print(string_to_print)
    return None

# Don't edit below this line

def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")

def main():
    test()

main()

#lesson 14
def calculate_experience_points(level):
    #xp = 0
    #for i in range(1, level):
    #    xp += 5 * i
    xp = 5 * level * ( level - 1 ) / 2
    return xp

#lesson 15
def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions > 0:
        mana += 1
        num_potions -= 1
    return mana, num_potions