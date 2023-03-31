from modulo_decoradores import *

@funcion_a
def suma_tres_valores(num1 = 0, num2 = 0, num3 = 0):
  """
    Función que imprime la suma de 3 valores
  """
  print(num1 + num2 + num3)
  
@funcion_a
def imprime_un_valor(valor:str):
  """
    Función que imprime un valor 
  """
  print(valor)