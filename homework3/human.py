class Human:
    def __init__(self, name=None, isSalesMan=False):
        self.Name = name
        self.isSalesMan = isSalesMan

    def __str__(self):
        return self.Name
