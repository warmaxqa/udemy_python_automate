from base_people import People

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

