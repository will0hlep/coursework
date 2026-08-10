#lesson 1
def number_sum(n):
    return 0.5 * n * ( n + 1 )

#lesson 2
def find_min(nums):
    min_found = float("inf")
    for num in nums:
        if num < min_found:
            min_found = num
    return min_found

#lesson 3
def remove_nonints(vals):
    nums = []
    for val in vals:
        if type(val) == int:
            nums.append(val)
    return nums

#lesson 4
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

#lesson 5
def area_sum(rectangles):
    area = 0
    for rectangle in rectangles:
        area += rectangle["height"] * rectangle["width"]
    return area

#lesson 6
def divide_list(nums, divisor):
    result = []
    for num in nums:
        result.append(num / divisor)
    return result

#lesson 7
def join_strings(strings):
    joined = ""
    for s in strings:
        joined += s + ","
    return joined[:-1]

#lesson 8
run_cases = [
    {
        "luck_boosts": [5, 3, 10],
        "expected_avg": 6.0,
    },
    {
        "luck_boosts": [7],
        "expected_avg": 7.0,
    },
    {
        "luck_boosts": [4, 4, 4],
        "expected_avg": 4.0,
    },
    {
        "luck_boosts": [2, 3],
        "expected_avg": 2.5,
    },
    {
        "luck_boosts": [],
        "expected_avg": 0,
    },
]

#lesson 9
def avg_luck_boost(luck_boosts):
    luck_boosts_length = len(luck_boosts)
    if luck_boosts_length == 0:
        return 0.
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / luck_boosts_length