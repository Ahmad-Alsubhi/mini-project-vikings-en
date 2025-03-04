import random

# Soldier


class Soldier:
    def __init__(self, health: int, strength: int):
        # your code here
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage


# Viking


class Viking(Soldier):
    def __init__(self, name: str, health: int, strength: int):
        # your code here
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        # your code here
        return "Odin Owns You All!" # I don't believe in this Odin man, only (Khalid bin Walid) The drawn sword of God 

    def receiveDamage(self, damage: int):
        # your code here
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon


class Saxon(Soldier):
    def __init__(self, health: int, strength: int):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage: int):
        # your code here
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# Davicente


class War:
    def __init__(self):
        # your code here

        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking:int):
        # your code here
        self.viking = viking
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon:int):
        # your code here
        self.saxon = saxon
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
