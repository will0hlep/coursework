#lesson 1
class Wall:
    armor = 10
    height = 5

class BatteringRam:
    damage = 2
    length = 4

#lesson 2
class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2

#lesson 3
class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    # don't touch below this line

    def fortify(self):
        self.armor *= 2

#lesson 6
class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

#lesson 8
def main():
    Aragorn = Brawler("Aragorn",4,4)
    Gimli = Brawler("Gimli",2,7)
    Legolas = Brawler("Legolas",7,7)
    Frodo = Brawler("Frodo",3,2)
    fight(Aragorn,Gimli)
    fight(Legolas,Frodo)

# don't touch below this line

class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength

def fight(attacker, defender):
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")

main()

#lesson 10
class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self):
        self.health -= 1
        if self.health <= 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows <= 0:
            raise Exception(f"{self.name} can't shoot")
        self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")
        target.take_hit()

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

#lesson 11
class Dragon:
    def __init__(self,element):
        self.element = element

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0

# don't touch below this line

def main():
    first_dragon = Dragon("fire")
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )

main()

#lesson 12
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        retained_books = []
        for i in self.books:
            if i.title != book.title or i.author != book.author:
                retained_books.append(i)
        self.books = retained_books

    def search_books(self, search_string):
        search_results = []
        search_string.lower()
        for i in self.books:
            if search_string in i.title.lower() or search_string in i.author.lower():
                search_results.append(i)
        return search_results