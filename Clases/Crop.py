'''
    summary: Clase para representar cada corte que es un digito encontrado en una
    Properties:
        img: matriz de pixeles
        id: posicion x en realcion a la imagen
'''
class Crop():
    def __init__(self, img, id):
        self.img = img
        self.id = id
