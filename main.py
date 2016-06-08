from Clases.RedNeuronal import *
from Clases.Imagen import Imagen
from Clases.Crops import Crops

imagen = Imagen('placa1.jpg')
imagen.aplicarFiltro()
crops = Crops('./Imagenes/descarga2.png')
crops.filterCrops()