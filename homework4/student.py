from human import Human
class Student(Human):
    def __init__(self, name, age, height, group, subject, grade ):
        super().__init__(name, age, height)
        self.__str__()