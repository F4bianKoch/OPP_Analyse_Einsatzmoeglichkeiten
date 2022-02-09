class Bauernhof:
    def __init__(self, bName):
        self.bName = bName
        self.animals = []

    def displayData(self):
        return f'Bauernhof Name: {self.bName}'

    def addAnimal(self, animal):
        self.animals.append(animal)


class Tier(Bauernhof):
    def __init__(self, bName, tName, tAge):
        super().__init__(bName)
        self.tName = tName
        self.tAge = tAge

    def displayData(self):
        return f'Mein Name ist {self.tName} und ich bin {self.tAge} Jahr/Jahre alt!'


class Kuh(Tier):
    def __init__(self, bName, tName, tAge):
        super().__init__(bName, tName, tAge)
        self.tArt = 'Kuh'

    def speak(self):
        print('Muu!')

    def __str__(self):
        return f'Kuh([Bauernhof_Instanz], {self.tName}, {self.tAge})'


class Schwein(Tier):
    def __init__(self, bName, tName, tAge):
        super().__init__(bName, tName, tAge)
        self.tArt = 'Schwein'

    def speak(self):
        print('grunz!')



bauernhof = Bauernhof('Infofarms')

obj_list = []
for obj in range(10):
    obj = Kuh(bauernhof, obj, '20')
    bauernhof.addAnimal(obj)
    obj_list.append(obj)


for obj in obj_list:
    print(obj.__str__())