

class Bauernhof:
    def __init__(self, bName, bOwner):
        self.bName = bName
        self.bOwner = bOwner

    def changeOwner(self, bOwner_new):
       self.bOwner = bOwner_new 

    def changeName(self, bName_new):
        self.bName = bName_new

    def displayData(self):
        return f'Bauernhof Name: {self.bName} \nBesitzer Name: {self.bOwner}'


class Tier(Bauernhof):
    def __init__(self, bName, bOwner, tID, tName, tFutter):
        super().__init__(bName, bOwner)