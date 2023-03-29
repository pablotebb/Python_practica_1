from modulo_decoradores import *


class ClaseVacia:
  pass 


class Super:
  def __init__(self, nombre_centro):
    self.__nombre_centro = nombre_centro
    self.__lista = []
    
  def get_listado(self):
    print("\nListado de la compra:")
    for i in range(len(self.__lista)):
      print(self.__lista[i])

  def agregar_articulo(self, articulo, cantidad):
    self.__lista.append({
      "articulo": articulo,
      "cantidad": cantidad 
    })  
    print(f"{articulo} --> {cantidad}")
  
    
    
  
    
    
