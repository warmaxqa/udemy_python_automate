class People():
    """"Родительский класс (основной)"""""

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """"Desctription our human"""""
        description = self.name + ", him " + str(self.age) + ", him height " + str(self.height) + ", him weight " + str(
            self.weight)
        print("New human named : " + description)

    def get_weight(self):
        """"Get weight man"""""
        print("Weight our human : " + str(self.weight))

    def get_height(self):
        print("Height our human : " + str(self.height))

    def update_weight(self, kg):
        """"Get update weight"""""
        self.weight = kg

    def update_height(self, cm):
        self.height = cm

class Warrior(People):
    """""Наследование класса People (потомок)"""""

    def __init__(self, name, age, height, weapon):
        super().__init__(name, age, height)
        self.rage = 100
        self.weapon = weapon


    def get_rage(self):
        """"Get rage warrior"""""
        print("Our rage is: " + str(self.rage))

    def description_warrior(self):
        """"Desctription our warrior"""""
        description = self.name + ", him " + str(self.age) + " years" +  " " +  "him height " + str(self.height)
        return description

    def get_weapon(self):
        description = self.name + " " + "and he got a " + self.weapon
        return description

class Mage(People):
    """""Наследование класса People (потомок)"""""

    def __init__(self, name, age, height, magic, mana):
        super().__init__(name, age, height)
        self.magic = magic
        self.mana = mana


    def get_mana(self):
        """"Get mana warrior"""""
        print("Our mana is: " + str(self.mana) + " %")

    def description_mage(self):
        """"Desctription our mage"""""
        description = self.name + ", him " + str(self.age) + " years" + " " + "him magic is " + self.magic + " and he got a" + " " + str(self.mana) + " " + "mana"
        return description

