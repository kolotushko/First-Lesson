from human import Human
class Worker(Human):
    def __init__(self, kindOfWorks = ""):
        self.KindOfWorks = kindOfWorks
    def __str__(self):
        return f"{super.__str__()}\n" \
               f"KindOfWorks: {self.KindOfWorks}"

