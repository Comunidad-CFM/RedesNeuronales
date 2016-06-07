from Clases.RedNeuronal import *
from Clases.Imagen import Imagen
from Clases.Crops import Crops

imagen = Imagen('placa4.jpg')
imagen.aplicarFiltro()
crops = Crops('./Imagenes/imagen.png')
crops.filterCrops()