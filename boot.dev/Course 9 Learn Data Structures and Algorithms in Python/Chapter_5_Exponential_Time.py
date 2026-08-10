#lesson 3
def fib(n):
    if n <= 1:
        return n
    current = 1
    parent = 0
    for i in range(n - 1):
        current, parent = current + parent, current
    return current

#lesson 4
def letter_combinations(digits):
    if digits == "":
        return []

    result = [""]

    for digit in digits:
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")

        letters = digit_to_letters[digit]
        new_result = []

        for combo in result:
            for letter in letters:
                new_result.append(combo + letter)

        result = new_result

    return result

# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

#lesson 10
def exponential_growth(n, factor, days):
    growth_sequence = [n]
    val = n
    for i in range(days):
        val *= factor
        growth_sequence.append(n)
    return growth_sequence