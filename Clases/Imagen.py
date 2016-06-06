from PIL import Image
import random

class Imagen:
    def __init__(self, imagen):
        self.__path = './Imagenes/'
        self.__imagen = Image.open(self.getPath() + imagen)
        self.__nombreSalida = 'imagen.png'

    def getPath(self):
        return self.__path

    def getImagen(self):
        return self.__imagen

    def getNombreSalida(self):
        return self.__nombreSalida

    def escalaGrises(self, imagen):
        pixeles = imagen.load()
        x, y = imagen.size

        for i in range(x):
            for j in range(y):
                (R, G, B) = pixeles[i, j]
                # Grayscale
                intensity = int((R + G + B) / 3)
                R = G = B = intensity
                pixeles[i, j] = (R, G, B)

    def filtroUmbral(self, imagen):
        imagen = self.getImagen()
        self.escalaGrises(imagen)
        pixeles = imagen.load()
        x, y = imagen.size

        for i in range(x):
            for j in range(y):
                (R, G, B) = pixeles[i, j]
                intensity = R
                if intensity < 128:
                    intensity = 0
                else:
                    intensity = 255

                R = G = B = intensity
                pixeles[i, j] = (R, G, B)

    def aplicarFiltro(self):
        self.filtroUmbral(self.getImagen())
        self.getImagen().save(self.getPath() + self.getNombreSalida())