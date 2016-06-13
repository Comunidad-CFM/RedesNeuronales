import difflib


class Similitud():
    def __init__(self, m, v, l):
        self.letras = l
        self.valores = v
        self.matrices = m

    def obtenerSimilitud(self, lista1, lista2):

        # s1 = [1, 0, 1, 0, 0, 0, 0, 1,0,0]
        # s2 = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
        sm = difflib.SequenceMatcher(None, lista1, lista2)
        return sm

    def comparar(self, evaluaciones, porcentaje):
        r = 0
        i = 0
        l = []
        for y in range(len(evaluaciones)):
            for x in range(len(self.matrices)):

                rAux = self.obtenerSimilitud(self.matrices[x][:porcentaje], evaluaciones[y][:porcentaje])
                if rAux > r:
                    r = rAux
                    l = self.matrices[x]
                    e = evaluaciones[y]
                    i = x
            print "Para la entrada"
            self.prettyPrint(l)
            print "Su mejor coincidencia es: " + self.letras[i][0] + " con un " + str(r.ratio() * 100) + "%"
            print "-------------------------------------\n"

    def prettyPrint(self, img):
        i = 0
        row = ''

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
