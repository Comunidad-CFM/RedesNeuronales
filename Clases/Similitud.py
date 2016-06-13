import difflib


class Similitud():
    def __init__(self):
        self.letras = []
        self.valores = []
        self.matrices = []

    def obtenerSimilitud(self, lista1, lista2):

        # s1 = [1, 0, 1, 0, 0, 0, 0, 1,0,0]
        # s2 = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1]
        sm = difflib.SequenceMatcher(None, lista1, lista2)
        return sm

    def comparar(self, entradas, evaluaciones, porcentaje):
        r = 0

        for x in range(len(entradas)):

            for y in range(len(evaluaciones)):

                rAux = self.obtenerSimilitud(entradas[x][:porcentaje], evaluaciones[y][:porcentaje])
                if rAux > r:
                    r = rAux
                    l = entradas[x]
            print r
