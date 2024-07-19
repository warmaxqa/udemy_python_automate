class Producers():
    """"Made producers"""""

    def __init__(self, name, labels, country):
        """"Initialization attributes"""""
        self.name = name
        self.labels = labels
        self.country = country

    def description_producers(self):
        """"Get parametrs producer"""""
        description = self.name + " " + self.labels + " " + self.country
        print(description)

    def get_country(self):
        print("Releases : " +  self.country)

    def get_labels(self):
        print("Labels for release : " + self.labels)

    def get_name(self):
        print("Name this prod : " + self.name)

prod = Producers ("Perez", "1985 , Shogun, 31", "New Zealand & England")
# prod.description_producers()
# prod.get_country()
# prod.get_labels()
prod.get_name()