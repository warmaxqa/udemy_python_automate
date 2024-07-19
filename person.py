class Person():
    """"Human model"""""

    def __init__(self, name, age):
        """"Initialization human atributes - name, age"""""
        self.age = age
        self.name = name


    def sing(self):
        """"Ask singing human"""""
        print(self.name + " singing")

    def dance(self):
        """"Ask dancing human"""""
        print(self.name + " dancing")

man =Person("Max",30)
woman =Person("Diana", 28)

man.dance()
woman.sing() 


