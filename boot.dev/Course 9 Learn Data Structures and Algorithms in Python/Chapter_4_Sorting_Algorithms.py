#lesson 1
class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

# dont touch above this line

def vanity(influencer):
    return 5 * influencer.num_bio_links + influencer.num_selfies

def vanity_sort(influencers):
    return sorted(influencers, key=vanity)

#lesson 2
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1,end):
            if nums[i-1] > nums[i]:
                swapping = True
                a = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = a
        end -= 1
    return nums

#lesson 6
def merge_sort(nums):
    nums_size = len(nums)
    if nums_size < 2:
        return nums
    sorted_left_half = merge_sort(nums[: nums_size // 2])
    sorted_right_half = merge_sort(nums[nums_size // 2 :])
    return merge(sorted_left_half, sorted_right_half)

def merge(first, second):
    final = []
    first_size = len(first)
    second_size = len(second)
    i = 0
    j = 0
    while i < first_size and j < second_size:
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    for k in range(i,first_size):
        final.append(first[k])
    for k in range(j,second_size):
        final.append(second[k])
    return final

#lesson 10
def insertion_sort(nums):
    list_length = len(nums)
    for i in range(1, list_length):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            temp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = temp
            j -= 1
    return nums

#lesson 15
def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

#lesson 22
def selection_sort(nums):
    list_size = len(nums)
    for i in range(list_size):
        smallest_idx = i
        for j in range(i + 1, list_size):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        if smallest_idx != i:
            nums[smallest_idx], nums[i] = nums[i], nums[smallest_idx]
    return nums