from modulo_decoradores import *


@funcion_d
def imprime_una_lista():
  """
    Función que imprime una lista
  """
  lista = [0, 1, 2, 3, 4, 5, 6, 7]
  print(lista)
  
@funcion_d 
def imprime_rango_de_ocho_elementos():
  """
    Función que imprime un rango de ocho elementos
  """
  my_rango = range(8)
  print("rango:", my_rango)
  my_lista = [i + 1 for i in my_rango]
  print("lista:", my_lista)
  
@funcion_d 
def imprime_rango_de_ocho_elementos_2():
  """
    Función que imprime un rango de ocho elementos, cambiando algo
  """
  my_rango = range(8)
  print("rango:", my_rango)
  my_lista = [sumatorio(i) for i in my_rango]
  print("lista:", my_lista)
  
def sumatorio(a):
  return a + 1