from modulo_decoradores import *
import math 
from math import pi as PI_VALUE
import my_module
from my_module import suma_tres_valores, imprime_un_valor


@funcion_d
def imprime_numero_pi():
  """
    Función que imprime el número PI
  """
  print(math.pi)
  
@funcion_d
def imprime_numero_pi_con_errors():
  """
    Función que imprime el número PI controlando los errores
  """
  try:
    print(math.pi)
  except AttributeError as e:
    print(f"Tienes este tipo de error: {e}")
  except Exception:
    print("Tienes un error")

@funcion_d
def imprime_numero_pi_2():
  """
    Función que imprime número pi, directamente, importando un valor
  """
  print(PI_VALUE)
  
@funcion_a
def imprime_valor_desde_modulo(valor:str):
  """
    Función que imprime un valor desde las funciones importadas de un módulo
  """
  imprime_un_valor(valor)
  
@funcion_a 
def imprime_valor_desde_un_modulo_2(valor:str):
  """
    Función que imprime un valor desde un módulo
  """
  my_module.imprime_un_valor(valor)
  
@funcion_a
def suma_tres_valores_desde_un_modulo(num1, num2, num3):
  """
    Función que suma 3 valores desde la función de un módulo
  """
  suma_tres_valores(num1, num2, num3)
  
@funcion_a
def suma_tres_valores_desde_un_modulo_2(num1, num2, num3):
  """
    Función que suma 3 valores desde un módulo
  """
  my_module.suma_tres_valores(num1, num2, num3)