from human import Human
from magasine import Magasine
humans = list()
novus  = Magasine("Novus")
max = Human("Max", True)
miroslav = Human("Miroslav")
alexander = Human("Alexander")
andrii = Human("Andrii")
oleg = Human("Oleg")
misha = Human("Misha")
vlad = Human("vlad")
humans.append(max)
humans.append(miroslav)
humans.append(alexander)
humans.append(andrii)
humans.append(oleg)
humans.append(misha)
humans.append(vlad)
for human in humans:
    novus.AddHumanToMagasine(human)
for salesman in novus.Seller:
    novus.ShowInfo(salesman)
for client in novus.Clients:
    novus.ShowInfo(client)
