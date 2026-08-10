#lesson 2
def find_max(nums):
    maximum = float("-inf")
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

#lesson 3
def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if full_name == f'{first_name} {last_name}':
                return True
    return False

#lesson 6
def get_avg_brand_followers(all_handles, brand_name):
    matching_handles = 0
    influencer_lists = 0
    for i in all_handles:
        influencer_lists += 1
        for j in i:
            if brand_name in j:
                matching_handles += 1
    return matching_handles/influencer_lists

#lesson 11
def find_last_name(names_dict, first_name):
    #for current_first_name, last_name in names_dict.items():
    #    if current_first_name == first_name:
    #        return last_name
    return names_dict[first_name] if first_name in names_dict else None

#lesson 12
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        if arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False

#lesson 13
def count_names(list_of_lists, target_name):
    count = 0
    for i in list_of_lists:
        for j in i:
            if target_name == j:
                count += 1
    return count