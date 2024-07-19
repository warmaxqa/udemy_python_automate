import base_people

man = base_people.People("Max", 30, 190)
man.description_person()

warrior = base_people.Warrior("RosUa", 29, 190, "Blade")
print("This warrior named : " + warrior.description_warrior())

mage = base_people.Mage("Lina", 666, 444, "Fire", 443)
print("This mage named : " + mage.description_mage())