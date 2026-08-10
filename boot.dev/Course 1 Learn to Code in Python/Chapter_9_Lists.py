#lesson 1
def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]

# Don't edit below this line

def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")

def main():
    test()

main()

#lesson 5
def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]
    item_index = 1
    return inventory[item_index]

#lesson 6
def get_last_index(inventory):
    return len(inventory)-1

#lesson 7
def smelt_ore(inventory):
    if inventory[1] == 'Iron Ore':
        inventory[1] = 'Iron Bar'
    return inventory

#lesson 8
def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

#lesson 9
def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")

def test():
    clear_inventory()
    print("=====================================")

def main():
    test()

main()

#lesson 10
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in items:
        if i == 'Potion':
            potion_count += 1
        elif i == 'Bread':
            bread_count += 1
        elif i == 'Shortsword':
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count

#lesson 13
def contains_leather_scraps(items):
    found = False

    for item in items:
        if item == 'Leather Scraps':
            found = True
            break

    return found

#lesson 14
def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)

# don't touch below this line

def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")

def main():
    test()

main()

#lesson 15
def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

#lesson 16
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        if i % 2 == 1:
            odd_numbers.append(i)

    return odd_numbers

#lesson 17
def get_champion_slices(champions):
    return champions[2:], champions[:-1], champions[::2]

#lesson 18
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    favourites = favorite_weapons + favorite_armor + favorite_items
    return favourites

#lesson 19
def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    return weapon in top_weapons

#lesson 20
def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    
#lesson 21
def get_heroes():
    heroes = [(
        "Glorfindel",
        2093,
        True),
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False)
    ]

    return heroes

#lesson 22
def get_first_item(items):
    if len(items)>0:
        return items[0]
    return 'ERROR'

#lesson 23
def reverse_list(items):
    return items[::-1]

#lesson 24
def filter_messages(messages):
    fucks_list = ['dang']
    unfucked_messages = []
    fucks_given = []
    for message in messages:
        message_words = message.split()
        of_our_lord = []
        fucks = []
        for word in message_words:
            if word in fucks_list:
                fucks.append(word)
            else:
                of_our_lord.append(word)
        unfucked_messages.append(' '.join(of_our_lord))
        fucks_given.append(len(fucks))
    return unfucked_messages, fucks_given

#lesson 25
def split_players_into_teams(players):
    return players[::2], players[1::2]

#lesson 26
def check_ingredient_match(recipe, inventory):
    missing = []
    count = 0
    for item in recipe:
        if item in inventory:
            count += 1
        else:
            missing.append(item)
    return 100*count/len(recipe), missing