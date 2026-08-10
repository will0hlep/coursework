#lesson 1
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = 100 * stamina
        self.mana = 10 * intelligence

#lesson 4
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    # don't touch above this line

    def get_fireballed(self, fireball_damage):
        self.health -= (fireball_damage - self.__stamina)

    def drink_mana_potion(self, potion_mana):
        self.mana += (potion_mana + self.__intelligence)

#lesson 7
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if self.mana < fireball_cost:
            raise Exception(f'{self.name} cannot cast fireball')
        self.mana -= fireball_cost
        target.get_fireballed(fireball_damage)

    def is_alive(self):
        return self.health > 0

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana

#lesson 8
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('cannot deposit zero or negative funds')
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('cannot withdraw zero or negative funds')
        elif self.__balance < amount:
            raise ValueError('insufficient funds')
        self.__balance -= amount