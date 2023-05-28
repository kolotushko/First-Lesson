class Human:
    def __init__(self, name="", age=0, height=0):
        self.Name = name
        self.Age = age
        self.Height = height

    def __str__(self):
        return f"Name: {self.Name}\n" \
               f"Age: {self.Age}\n" \
               f"Height: {self.Height}"





