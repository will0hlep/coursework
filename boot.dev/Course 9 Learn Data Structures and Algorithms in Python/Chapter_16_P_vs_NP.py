#lesson 3
def tsp(cities, paths, dist):
    n = len(cities)
    walks = permutations(cities)
    for walk in walks:
        walk_dist = 0
        for i in range(n-1):
            walk_dist += paths[walk[i]][walk[i+1]]
        if walk_dist < dist:
            return True
    return False

# don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res

def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

#lesson 4
def verify_tsp(paths, dist, actual_path):
    n = len(actual_path)
    path_dist = 0
    for i in range(n-1):
        path_dist += paths[actual_path[i]][actual_path[i+1]]
    return path_dist < dist

#lesson 9
def get_num_guesses(length):
    #result = 0
    #for i in range(length):
    #    result += 26 ** (i + 1)
    #return result
    return 26 * (26 ** length - 1) / 25

#lesson 16
import math

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    test_val = 3
    test_lim = math.sqrt(n)
    while n > 1:
        if n % test_val == 0:
            factors.append(test_val)
            n /= test_val
            test_val = 3
        else:
            test_val += 2
            if test_lim < test_val:
                factors.append(n)
                n = 1
    return factors

#lesson 20
def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) - 1)

def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    elif index < 0:
        return False
    elif nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    return (
            find_subset_sum(nums, target, index - 1)
            or
            find_subset_sum(nums, target - nums[index], index - 1)
    )