# challenge 1

starting_gold = 500
sword_cost = 120
shield_cost = 80
bonus_gold = 50

total_cost = sword_cost + shield_cost
gold_left_after_buying = starting_gold - total_cost
final_gold = gold_left_after_buying + bonus_gold

print(starting_gold)
print(total_cost)
print(gold_left_after_buying)
print(final_gold)

# challenge 2
def can_start_quest(player_level, required_level, has_sword, has_shield, is_banned):
    if player_level >= required_level:
        if has_sword:
            if not is_banned:
                if has_shield:
                    return True
                elif player_level >= required_level + 5:
                    return True
    return False

#challenge 3
def build_inventories(events):
    inventories = {}
    for event in events:
        player = event["player"]
        item = event["item"]
        if player not in inventories:
            inventories[player] = {item : 1}
        elif item not in inventories[player]:
            inventories[player][item] = 1
        else:
            inventories[player][item] += 1
    return inventories

#challenge 4
def get_shared_games(friend1_games, friend2_games):
    set1 = set(friend1_games)
    set2 = set(friend2_games)
    shared = set1.intersection(set2)
    result = list(shared)
    result.sort()
    return result


def get_all_games(friend1_games, friend2_games):
    set1 = set(friend1_games)
    set2 = set(friend2_games)
    all_games_set = set1.union(set2)
    result = list(all_games_set)
    result.sort()
    return result

#challenge 5
def safe_pick(players, index):
    try:
        if type(players) != list:
            raise TypeError
        else:
            return players[index]
    except TypeError:
        return "No player list"
    except:
        return "No player"

#challenge 6
def format_username(username):
    username = username.lower().strip()
    return username

def make_inbox_label(username, unread_count):
    if unread_count <= 0:
        return username + " (no unread messages)"
    return username + " (" + str(unread_count) + " unread)"

def build_notification(username, unread_count):
    label = make_inbox_label(format_username(username), unread_count)
    return "Inbox for " + label

#challenge 7
def grade_quizzes(student_answers, correct_answers):
    grades = []
    questions = len(correct_answers)
    for i in student_answers:
        score = 0
        for j in range(questions):
            if i[j] == correct_answers[j]:
                score += 4
            elif i[j] != '' and i[j] is not None:
                score -= 1
        grades.append(score)
    return grades

#challenge 8
class BankAccount:
    def __init__(self, owner, starting_balance):
        self.owner = owner
        self.__balance = starting_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def transfer_to(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False
    
#challange 9
def analyze_attendance(day1_attendees, day2_attendees):
    day1_set = set(day1_attendees)
    day2_set = set(day2_attendees)

    all_attendees = day1_set.union(day2_set)
    both_days = day1_set.intersection(day2_set)
    only_day1 = day1_set.difference(day2_set)
    only_day2 = day2_set.difference(day1_set)
    
    return {
        "unique_count" : len(only_day1) + len(both_days) + len(only_day2),
        "both_days" : both_days,
        "only_day1" : only_day1,
        "only_day2" : only_day2
    }

#challenge 10
def summarize_book_ratings(reviews):
    summary_dictionary = {}
    for review in reviews:
        book_id = review["book_id"]
        if type(book_id) == str:
            try:
                rating = review["rating"]
                if rating in [1,2,3,4,5]:
                    if book_id not in summary_dictionary:
                        summary_dictionary[book_id] = {}
                        summary_dictionary[book_id]["count"] = 1
                        summary_dictionary[book_id]["total"] = rating
                    else:
                        summary_dictionary[book_id]["count"] += 1
                        summary_dictionary[book_id]["total"] += rating
            except KeyError:
                continue
    for book_id in summary_dictionary:
        summary_dictionary[book_id]["average"] = summary_dictionary[book_id]["total"] // summary_dictionary[book_id]["count"]
    return summary_dictionary

#challenge 11
import math

def hypotenuse(a, b):
    c_squared = a * a + b * b
    return math.sqrt(c_squared)

#challenge 12
def transform_playlist(durations, filter_fn, transform_fn):
    return list(map(transform_fn, filter(filter_fn, durations)))

#challenge 13
def total_duration(plan):
    if 'duration' in plan:
        return plan['duration']
    duration = 0
    if plan['mode'] == 'sequential':
        for step in plan['steps']:
            duration += total_duration(step)
    if plan['mode'] == 'parallel':
        for step in plan['steps']:
            if total_duration(step) > duration:
                duration = total_duration(step)
    return duration

#challenge 14
def apply_loyalty_discount(prices, base_discount_percent):
    # Do not modify the input list. Create a new result list.
    result = []
    final_discount = base_discount_percent
    # Use integer math and round .5 up for ties.
    # For each price: discounted = round_half_up(price * (100 - final_discount) / 100)
    for price in prices:
        numerator = price * (100 - final_discount)
        # Add 50 to implement .5-up rounding when dividing by 100
        discounted = (numerator + 50) // 100
        result.append(discounted)
    return result

#challenge 15
from dataclasses import dataclass
from typing import Union

@dataclass
class TextMessage:
    sender: str
    content: str

@dataclass
class ImageMessage:
    sender: str
    url: str
    caption: str

@dataclass
class SystemMessage:
    code: int
    message: str

Message = Union[TextMessage, ImageMessage, SystemMessage]

def render_message(msg: Message) -> str:
    match msg:
        case TextMessage(sender=sender, content=content):
            return f"{sender} says: {content}"
        case ImageMessage(sender=sender, url=url, caption=caption):
            return f"{sender} sent an image: {url} ({caption})"
        case SystemMessage(code=code, message=message):
            return f"[SYSTEM {code}] {message}"
        case _:
            raise ValueError
        
#challenge 16
def validate_non_negative(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == int or type(arg) == float:
                if arg < 0:
                    raise ValueError("negative argument")
        for kwarg in kwargs:
            for i in kwargs:
                if type(kwargs[i]) == int or type(kwargs[i]) == float:
                    if kwargs[i] < 0:
                        raise ValueError("negative argument")
        return func(*args, **kwargs)
    return wrapper

def cache_results(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if (args, tuple(sorted(kwargs.items()))) in cache:
            return cache[(args, tuple(sorted(kwargs.items())))]
        result = func(*args, **kwargs)
        cache[(args, tuple(sorted(kwargs.items())))] = result
        return result
    return wrapper

#challenge 17
def count_above_threshold(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count

#challenge 18
def make_score_tracker(start_score):
    score = start_score
    def inner_func(points):
        nonlocal score
        score += points
        if score < 0:
            score = 0
        return score
    return inner_func

#challenge 19
from enum import Enum

class TaskResultType(Enum):
    SUCCESS = "success"
    NOT_FOUND = "not_found"
    PERMISSION_DENIED = "permission_denied"
    VALIDATION_ERROR = "validation_error"

def format_task_result(result):
    match result["type"]:
        case TaskResultType.SUCCESS:
            return f"Task {result["task_id"]} completed successfully."
        case TaskResultType.NOT_FOUND:
            return f"Task {result["task_id"]} was not found."
        case TaskResultType.PERMISSION_DENIED:
            return f"User {result["user"]} cannot access task {result["task_id"]}."
        case TaskResultType.VALIDATION_ERROR:
            return f"Task {result["task_id"]} has validation errors: {", ".join(result["errors"])}"

#challenge 20
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return Node(value)
    if root.value >= value:
        root.left = insert_bst(root.left, value)
    if root.value < value:
        root.right = insert_bst(root.right, value)
    return root


def inorder_values(root):
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.value)
        traverse(node.right)

    traverse(root)
    return result

#challenge 21
TOMBSTONE = object()

def string_hash(key, capacity):
    h = 0
    for ch in key:
        h *= 31
        h += ord(ch)
        h %= capacity
    return h

class HashMap:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.fill = 0
        self.keys = [None for i in range(self.capacity)]
        self.values = [None for i in range(self.capacity)]

    def __len__(self):
        return self.fill

    def set(self, key, value):
        hash = string_hash(key, self.capacity)
        for i in range(hash, hash + self.capacity):
            index = i % self.capacity
            if self.keys[index] == key:
                self.values[index] = value
                break
            elif self.keys[index] is None or self.keys[index] == TOMBSTONE:
                self.fill += 1
                if self.fill/self.capacity > 0.7:
                    self.resize()
                self.keys[index] = key
                self.values[index] = value
                break

    def resize(self):
        tmp_key = self.keys
        tmp_val = self.values
        tmp_cap = self.capacity
        self.capacity *= 2
        self.keys = [None for i in range(self.capacity)]
        self.values = [None for i in range(self.capacity)]
        for i in range(tmp_cap):
            if tmp_key[i] is not None and tmp_key[i] != TOMBSTONE:
                hash = string_hash(tmp_key[i], self.capacity)
                for j in range(hash, hash + self.capacity):
                    index = j % self.capacity
                    if self.keys[index] is None:
                        self.keys[index] = tmp_key[i]
                        self.values[index] = tmp_val[i]
                        break

    def get(self, key, default=None):
        hash = string_hash(key, self.capacity)
        for i in range(hash, hash + self.capacity):
            index = i % self.capacity
            if self.keys[index] == key:
                return self.values[index]
        return default

    def delete(self, key):
        hash = string_hash(key, self.capacity)
        for i in range(hash, hash + self.capacity):
            index = i % self.capacity
            if self.keys[index] == key:
                self.keys[index] = TOMBSTONE
                self.values[index] = None
                self.fill -= 1
                break

#challenge 22
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_value

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
    
#challenge 23
def bfs_traversal(graph, start):
    if start not in graph:
        return []
    visited_vertices = []
    to_be_explored = [start]
    while to_be_explored != []:
        current = to_be_explored[0]
        to_be_explored.pop(0)
        visited_vertices.append(current)
        for next in graph[current]:
            if next not in visited_vertices:
                if next not in to_be_explored:
                    to_be_explored.append(next)
    return visited_vertices

def dfs_traversal(graph, start):
    if start not in graph:
        return []
    visited_vertices = []
    visited_vertices = depth_first_search_r(visited_vertices, graph, start)
    return visited_vertices

def depth_first_search_r(visited, graph, current_vertex):
    visited.append(current_vertex)
    neighbors = graph[current_vertex]
    for vertex in neighbors:
        if vertex not in visited:
            depth_first_search_r(visited, graph, vertex)
    return visited

#challenge 24
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_level = self.root
        for char in word:
            if char not in current_level.children:
                current_level.children[char] = TrieNode()
            current_level = current_level.children[char]
        current_level.is_word = True

    def contains(self, word):
        current_level = self.root
        for char in word:
            if char not in current_level.children:
                return False
            current_level = current_level.children[char]
        return current_level.is_word

    def starts_with(self, prefix):
        current_level = self.root
        for char in prefix:
            if char not in current_level.children:
                return False
            current_level = current_level.children[char]
        return True

    def get_words_with_prefix(self, prefix):
        current_level = self.root
        for char in prefix:
            if char not in current_level.children:
                return []
            current_level = current_level.children[char]
        return check_level(current_level, prefix)

def check_level(level, prefix):
    words = []
    if level.is_word:
        words.append(prefix)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in level.children:
            words.extend(check_level(level.children[char], prefix+char))
    return words

def build_trie(words):
    trie = Trie()
    for w in words:
        trie.insert(w)
    return trie

#challenge 25
TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode(text={self.text!r}, text_type={self.text_type!r}, url={self.url!r})"


class HTMLNode:
    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}

    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for key in self.props:
            value = self.props[key]
            result += f" {key}=\"{value}\""
        return result


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.tag is None:
            return self.value

        if self.tag == "img":
            props_html = self.props_to_html()
            return f"<img{props_html}>"

        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"


def text_node_to_html_node(text_node):
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {'href': text_node.url})

    if text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode("img", '', {'src': text_node.url, "alt": text_node.text})

    raise Exception("Unknown text type")

#challenge 26
class Unit:
    def get_power(self):
        raise NotImplementedError()

    def __add__(self, other):
        return self.get_power() + other.get_power()


class Warrior(Unit):
    def __init__(self, strength, weapon_bonus):
        self.strength = strength
        self.weapon_bonus = weapon_bonus

    def get_power(self):
        return self.strength + self.weapon_bonus


class Mage(Unit):
    def __init__(self, intelligence, spell_level):
        self.intelligence = intelligence
        self.spell_level = spell_level

    def get_power(self):
        return self.intelligence + (self.spell_level * 2)


class Archer(Unit):
    def __init__(self, dexterity, arrow_count):
        self.dexterity = dexterity
        self.arrow_count = arrow_count

    def get_power(self):
        return self.dexterity + (self.arrow_count // 5)


def get_team_power(units):
    power = 0
    for unit in units:
        power += unit.get_power()
    return power
