#lesson 2
def find_minimum(nums):
    if nums == []:
        return None
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

#lesson 5
def summed(nums):
    total = 0
    for num in nums:
        total += num
    return total