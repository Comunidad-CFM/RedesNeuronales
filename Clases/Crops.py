import cv2, numpy
from Crop import Crop

'''
    summary: Clase cuya funcionalidad es encargarse de recortar los digitos encontrados en una imagen
                y darle el tratamiento necesario para pasar a la fase de analisis en la red neuronal
    Properties:
        im: imagen original
        crops: lista de matrices que representan los recortes encontrados
        images: lista con las matrices de las imagenes mas importantes
        imagesBinary: lista con las matrices de imagenes final, en la que se encuentran los valores binarizados y redimensionados
'''
class Crops():
    def __init__(self, imagen):
        # Leer y filtrar la imagen para recontar
        self.im = cv2.imread(imagen)
        self.gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)

        self.thresh = cv2.adaptiveThreshold(self.gray, 255, 1, 1, 11, 2)
        self.image, self.contours, self.hierarchy = cv2.findContours(self.thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # fin de Leer y filtrar imagen para recortar
        self.crops = []
        self.images = []
        self.imagesBinary = []

    '''
        summary: Funcion para ordenar los recortes utilizando el metodo burbuja
    '''
    def sortCrops(self):
        length = len(self.crops)
        temp = 0

        for i in range(0, length):
            for j in range(0, length - 1):
                if (self.crops[j].id > self.crops[j + 1].id):
                    temp = self.crops[j]
                    self.crops[j] = self.crops[j + 1]
                    self.crops[j + 1] = temp

            length -= 1

    '''
        summary: Funcion que recorre la imagen original y la recorta los digitos que encuentre
    '''
    def cutImage(self):
        for cnt in self.contours:
            if cv2.contourArea(cnt) > 50:
                [x, y, w, h] = cv2.boundingRect(cnt)

                if h > 28:
                    roi = self.im[y:y + h, x:x + w]
                    self.crops.append(Crop(roi, cnt[0][0][0]))

    '''
        summary: obtener el promedio para los valores x,y de los recortes realizados en cutImage
    '''
    def getAverage(self):
        x = 0
        y = 0

        for i in self.crops:
            x += len(i.img[0])
            y += len(i.img)

        x = x / len(self.crops)
        y = y / len(self.crops)

        return x, y

    '''
        summary: Filtrar los recortes que se encuentran dentro de los rangos de los promedios
    '''
    def canInsert(self, img):
        for crop in self.crops:
            if (img.id > crop.id - 10) and (img.id < crop.id + 10):
                return False

        img.img = i = cv2.resize(img.img, (100, 200))
        self.crops.append(img)
        return True

    '''
        summary: determinar si en un bloque de pixeles se encuentra un 1, si lo encuentra devuelve 1, sino 0
            :param img, bloque de pixeles a analizar
            :return 1 si hay 1 en algun sector del bloque 0 si no
    '''
    def haveBlack(self, img):
        for row in img:
            for pixel in row:
                if not numpy.all([pixel, [255,255,255]]):
                    return 1
        return 0

    '''
        summary: imprimir las matrices finales una vez terminado el proceso.
    '''
    def prettyPrint(self):
        i = 0
        row = ''
        for img in self.imagesBinary:
            print"imagen", img
            for i in range(0, len(img)):
                if i % 10 == 0:
                    print row
                    row = ''
                if img[i] == 1:
                    row += '*'
                else:
                    row += ' '
            print row
            row = ''
            print

    '''
        summary: recorre las matrices y les aplica una redimension si en el grupo de pixeles seleccionado existe un
                    1 o 0

    '''
    def binarization(self):
        list = []
        for crop in self.crops:
            for x in range(0, 200, 20):
                for y in range(0, 100, 10):
                    list.append(self.haveBlack(crop.img[x:x+20, y:y+10]))
            self.imagesBinary.append(list)
            list = []

    '''
        summary: filtra la lista de recortes para seleccionar unicamente los digitos que importan, que son los que se encuentran
                    dentro del rango
    '''
    def filterCrops(self):
        self.cutImage()
        self.sortCrops()
        j = 0
        x, y = self.getAverage()

        for i in self.crops:
            if (len(i.img[0]) >= x and len(i.img[0]) <= x + (x * 0.25)) or (len(i.img) >= y and len(i.img) <= y + (y * 0.25)):
                self.images.append(i)

        self.crops = []

        for i in self.images:
            if self.canInsert(i):
                cv2.imwrite('./crops/' + str(j) + '.png', i.img)
                j += 1

        self.binarization()
        self.prettyPrint()

        #print "-----------------------"
        #print x, y
        #cv2.waitKey(0);
