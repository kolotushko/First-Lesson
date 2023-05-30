from student import Student
from Worker import Worker
class Friend(Student, Worker):
    def __init__(self, name, age, height, group, subject, grade, kindOfWorks):
        super().__init__(name, age, height, group, subject, grade)
        self.kindOfWorks = kindOfWorks
    def __str__(self):
        return f"{super().__str__()}\n"  \
               f"{self.ShowInfo(self.kindOfWorks)}"
