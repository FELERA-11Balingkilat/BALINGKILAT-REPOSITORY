#Hero class
class Heroes:
    def __init__(self,name,hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount
        print(self.name, "has", self.hp, "hp left.")

name = Heroes("Arthur")
name2 = Heroes("Morgana")

name.take_damage(10)
name2.take_damage(0)
