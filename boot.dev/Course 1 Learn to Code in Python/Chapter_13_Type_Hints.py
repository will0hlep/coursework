#lesson 2
character_name: str = "Gandalf"
character_level: int = 80
character_health: float = 99.5
has_magic: bool = True

#lesson 3
def get_character_status(name: str, level: int, health: float, has_magic: bool) -> str:
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status

#lesson 4
def get_item_description(item_name: str, damage: int, is_magical: bool) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description

#lesson 5
def get_greeting(player_name: str) -> str:
    return f"Welcome to Fantasy Quest, {player_name}!"

#lesson 6
def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items

#lesson 7
def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0

#lesson 8
def get_loot_drop(enemy_level: int) -> tuple[str,int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3

#lesson 9
def get_reward_summary(items: list[str], item_counts: dict[str,int]) -> tuple[str,int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items

#lesson 11
def summon_mount(has_mount: bool, distance: int) -> str|None:
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"

#lesson 12
def summarize_quest_rewards(
    completed_quests: list[str], quest_rewards: dict[str, int]
) -> list[tuple[str, int]]:
    summary: list[tuple[str, int]] = []

    for quest_name in completed_quests:
        if quest_name in quest_rewards:
            quest_xp = quest_rewards[quest_name]
            summary.append((quest_name,quest_xp))

    return summary
