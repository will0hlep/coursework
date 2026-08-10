#lesson 1
def remove_duplicates(spells):
    return list(set(spells))

#lesson 5
def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0
    unique = set()
    for char in text:
        if char in vowels:
            count += 1
            unique.add(char)
    return count, unique

#lesson 6
def find_missing_ids(first_ids, second_ids):
    return set(first_ids) - set(second_ids)