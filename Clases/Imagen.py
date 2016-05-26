from PIL import Image

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
        pic = imagen.load()

        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                (R, G, B) = pic[i, j]
                # Grayscale
                intensity = int((R + G + B) / 3)
                R = G = B = intensity
                pic[i, j] = (R, G, B)
        return pic

    def filtroUmbral(self, imagen):
        self.escalaGrises(imagen)
        pic = imagen.load()

        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                (R, G, B) = pic[i, j]
                intensity = R
                if intensity < 128:
                    intensity = 0
                else:
                    intensity = 255
                R = G = B = intensity
                pic[i, j] = (R, G, B)

        return pic

    def aplicarFiltro(self):
        pic = self.filtroUmbral(self.getImagen())
        self.getImagen().save(self.getPath() + self.getNombreSalida())