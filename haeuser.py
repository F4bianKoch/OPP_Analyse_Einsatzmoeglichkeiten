class Haeuser:
    def __init__(self, farbe, zimmer, hoehe):
        self.farbe = farbe
        self.zimmer = zimmer
        self.hoehe = hoehe

    def displayData(self):
        return f'Farbe: {self.farbe}; Zimmer: {self.zimmer}; Hoehe: {self.hoehe}'


haus1 = Haeuser('Blau', 8, 15)
print(haus1.displayData())