from human import Human
class Magasine:
    def __init__(self, brand=None):
        self.Brand = brand
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
            if(human.isSalesMan):
                print(f"The salesman of the magasine {self.Brand} is: {human.Name}")
            else:
                print(f"The client of the magasine {self.Brand} is: {human.Name}")

