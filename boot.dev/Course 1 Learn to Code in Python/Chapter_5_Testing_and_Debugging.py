#lesson 1
def total_xp(level, xp_to_add):
    return 100*level + xp_to_add

#lesson 3
def take_magic_damage(health, resist, amp, spell_power):
    health -= spell_power * amp - resist
    return health

#lesson 7
def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert = f'Achievement Unlocked: {ach_name}'
    return after_xp, alert

#lesson 8
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f'You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.'
    return msg