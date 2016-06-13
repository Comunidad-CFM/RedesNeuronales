# class RedNeuronal:
#     def __init__(self):
#         self.__saludo = "Hola mundo!"
#
#     def getSaludo(self):
#         return self.__saludo
#
#
#
import cPickle #Permite guardar y abrir archivos rapidamente
from numpy import *
import os

class nn:
    def sigmoid(self,x):
        return tanh(x)
    # derivada de la funcion sigmoid
    def dsigmoid(self,y):
        #d/dx(tanh(x))=1 - (tanh(x))^2
        return 1.0-y*y

    def __init__(self, ni, nh, no):
        self.resultadoEvaluacion = []
        self.resultadoEntrenamiento = []

        # numero de nodos entrada, oculta y salidas
        self.ni = ni +1 # +1 para los bias
        self.nh = nh
        self.no = no

        # activacion de los nodos
        self.ai = ones((self.ni))
        #print self.ai
        self.a1 = ones((self.nh))
        #print self.a1
        self.ao = ones((self.no))
        #print self.ao

        # crear pesos
        self.w1 = random.uniform(-1.0,1.0,(self.ni, self.nh))
        #print self.w1
        self.w2 = random.uniform(-1.0,1.0,(self.nh, self.no))
        #print self.w2


    def guardar(self,filename):
         W = [self.w1,self.w2]
         cPickle.dump(W,open(filename,'w'))

    def cargar(self,filename):
         W = cPickle.load(open(filename,'r'))
         self.w1=W[0]
       #  print self.w1
         self.w2=W[1]
      #   print self.w2

    def evaluar(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError, 'numero erroneo de entradas'

      #  print("activaciones entradas")
        self.ai[0:self.ni-1]=inputs
     #   print self.ai[0:self.ni-1]

      #  print("acticaciones capa oculta")
      #  print("a1=f1(W1*p)")
        self.n1 = dot(transpose(self.w1),self.ai)
      #  print self.n1
        self.a1= self.sigmoid(self.n1)
       # print self.a1

      #  print(" activaciones salidas")
       # print("a2=f2(W2* a1)")
        self.n2 = dot(transpose(self.w2),self.a1)
       # print ("salida de la red")
        self.ao = self.sigmoid(self.n2)

        return self.ao

    def backPropagate(self, targets, N):
        if len(targets) != self.no:
            raise ValueError, 'numero de objetivos incorrectos'

      #  print("Propagar errores hacia atras")
      #  print("Calcular errores a la salida")
        d2=targets-self.ao
       # print d2

      #  print("Calcular errores en la capa oculta")
        d1 = dot(self.w2,d2)
       # print d1

      #  print ("Acutalizar pesos de la salida")
      #  print ("Wnuevo += Wviejo+n*(delta2*f2')*a1")
        d2fp= self.dsigmoid(self.ao) * d2
       # print d2fp
        change = d2fp * reshape(self.a1,(self.a1.shape[0],1))
       # print change
        self.w2 = self.w2 + N * change
       # print self.w2

       # print("Actualizar pesos de las entradas")
       # print("Wnuevo += Wviejo+n*(delta1*f1')*a0")
        d1fp =self.dsigmoid(self.a1) * d1
       # print d1fp
        change = d1fp * reshape(self.ai,(self.ai.shape[0],1))
       # print change
        self.w1 = self.w1 + N * change
       # print self.w1

        #calcular error
        error = sum(N * (targets - self.ao) ** 2)

        return error

    def test(self, entrada, metodo):
        print("Imprime la entrada y su salida de la red neuronal")
        for p in range(size(entrada,axis=0)):
            inputAux = entrada[p, :]
            evaluate = self.evaluar(entrada[p,:])
            if (metodo == 1):
                self.resultadoEntrenamiento.append((inputAux, evaluate))
            else:
                self.resultadoEvaluacion.append((inputAux, evaluate))
            print inputAux, '->', evaluate

    def train(self, entrada, salida, iterations=50000, N=0.15):
        print("Realiza entrenamiento backpropagation")
        # N: factor de aprendizaje
        itera = 0
        for i in xrange(iterations):
            error = 0.001
            for p in range(size(entrada,axis=0)):
                inputs = entrada[p,:]
                targets = salida[p,:]
                self.evaluar(inputs)
                error = error + self.backPropagate(targets, N)
            if i % 100 == 0 and i!=0:
                print 'iteracion:   ' + str(iterations -i) + '  -   error ' + str(error)
                itera += 1

        print ("")
        print ("numero de iteracion final")
        print itera

        # def getoutput(self, inputslen):
        #     output = []
        #     base = -0.1
        #     for i in xrange(inputslen):
        #         output.append([base])
        #         base += 0.03
        #     return output





#
# def main():
#
#     print ("Opciones para la red neuronal")
#     print ("1. entrenamiento y guardar datos")
#     print ("2. cargar datos y simular la red")
#     print ("3. salir")
#     prueba = nn(100, 5, 1)
#
#     while True:
#         op = raw_input("Elegir una opcion: ")
#
#         if(op == '1'):#5, 6, 7, 8, 9
#             prueba = nn(1,36,1)
#             entradas = array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#                               [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#                               [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#                               [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]])
#             a = []
#             b = []
#             c = 0.01
#             for x in range(10):
#
#                 a.append([x+1])
#                 b.append([c])
#                 c += 0.1
#             print a
#             print b
#
#             entradas = array(a)
#             salida = array(b)
#
#             print("COMIENZA ENTRENAMIENTO")
#             print("")
#             prueba.train(entradas,salida)
#
#             print("")
#             prueba.test(entradas)
#             print("Se ha guardado el entrenamiento correctamente con el nombre de entrenamiento.txt")
#
#             print("")
#             prueba.guardar("entrenamiento.txt")
#             print("")
#             break
#
#         elif(op == '2'):
#             print("")
#             prueba = nn(100,5,1)
#             print("se cargan los pesos y el proceso se hace interno")
#             prueba.cargar("entrenamiento.txt")
#             print("")
#
#             print("RED ENTRENADA")
#             print("COMIENZA LA SIMULACION")
#             print("")
#             #entradasTest = array([[3.5,3.6],[3.2,3.3],[3.8,3.7],[3.6,3.5],[3.4,3.3],[3.3,3.2],[3.4,3.4],[3.7,3.6]])
#             entradasTest = array([[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]])
#
#             prueba.test(entradasTest)
#             break
#
#         elif(op == '3'):
#             break
#         else:
#             print ("")
#             raw_input("No has pulsado ninguna opcion correcta.. \npulsa una tecla para continuar")
#main()
