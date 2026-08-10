#lesson 1
def get_estimated_spread(audiences_followers):
    count = len(audiences_followers)
    if count == 0:
        return 0
    total = 0
    for follows in audiences_followers:
        total += follows
    return total * count ** 0.2

#lesson 4
def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        growth_rate = 4
    elif influencer_type == "cosmetic":
        growth_rate = 3
    else:
        growth_rate = 2
    return follower_count * growth_rate ** num_months

#lesson 7
import math

def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)

#lesson 11
def num_possible_orders(num_posts):
    product = 1
    for i in range(1, num_posts):
        product *= i+1
    return product

#lesson 14
def decayed_followers(initial_followers, fraction_lost_daily, days):
    return initial_followers * (1-fraction_lost_daily) ** days

#lesson 15
import math

def log_scale(data, base):
    new_data = []
    for val in data:
        new_data.append(math.log(val, base))
    return new_data

#lesson 16
def average_followers(nums):
    count = len(nums)
    if count == 0:
        return None
    total = 0
    for num in nums:
        total += num
    return total/count