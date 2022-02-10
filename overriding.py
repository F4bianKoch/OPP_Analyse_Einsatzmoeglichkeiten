class Mobile:
    def takePicture(self):
        print('Bild gemacht!')


class Samsung(Mobile):
    def takePicture(self, camera):
        print(f'Bild mit {camera} gemacht')

class iPhone(Mobile):
    pass
    

s1 = Samsung()
s1.takePicture('superwide Kamera')
i1 = iPhone()
i1.takePicture()