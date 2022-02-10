# Mensch erstellen mit SP

mensch1 = ['Bill', 40, 'Müllmann']


# Mensch erstellen mit OOP

class Mensch:
    def __init__(self, name, alter, job):
        self.name = name
        self.alter = alter
        self.job = job

    
menschOOP = Mensch('Adrian', 18, 'CEO')
print(menschOOP.name)