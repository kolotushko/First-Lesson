from human import Human
class Shop:

    def __init__(self, NameMagasine=None):
        self.NameMagasine = NameMagasine
        self.Clients = list()
        self.Seller = list()
    def AddHumanToMagasine(self, human = Human()):
        if(isinstance(human, Human) and human  != None):
            if(human.isSalesMan):
                self.Seller.append(human)
            else:
                self.Clients.append(human)
    def ShowInfo(self, human = Human()):
        if(isinstance(human, Human) and human  != None):
            print(f"The SalesMan of the Shop {self.NameMagasine} is: {human.Name}")
        else:
            print(f"The Client of the Shop {self.NameMagasine} is: {human.Name}")

