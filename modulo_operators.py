from modulo_decoradores import *

@funcion_a
def suma(num1=0, num2=0):
  """
    Funcion que suma 2 números
  """
  print(num1 + num2)

@funcion_a
def resta(num1=0, num2=0):
  """
    Funcion que resta 2 números
  """
  print(num1 - num2)

@funcion_a
def multiplicacion(num1=0, num2=0):
  """
    Funcion que multiplica 2 números
  """
  print(num1 * num2)

@funcion_a
def division_decimal(num1=0, num2=0):
  """
    Funcion que divide 2 números
  """
  print(num1 / num2)

@funcion_a
def division_entera(num1=0, num2=0):
  """
    Funcion que divide 2 números
  """
  print(num1 // num2)

@funcion_a
def modulo(num1=0, num2=0):
  """
    Funcion que devuelve el resto de 2 números
  """
  print(num1 % num2)
  
@funcion_d
def imprime_cadena_con_numero():
  """
    Funcion que imprime una cadena, concatenándolo con un número
  """
  cadena = "Hola como estás, eres el: "
  numero = 1 
  print(cadena + str(numero))
  print(f"{cadena} {numero}")
  
@funcion_d
def imprime_cadena_tantas_veces():
  """
    Función que imprime una cadena un número determinado de veces
  """
  print("Hola " * 5)
  print("Adios " * (2**3))
  
@funcion_a
def imprime_operaciones_con_enteros(a=0, b=0):
  """
    Función que imprime operaciones con enteros
  """
  print(f"{a} > {b}: ", a > b)
  print(f"{a} < {b}: ", a < b)
  print(f"{a} >= {b}: ", a >= b)
  print(f"{a} <= {b}: ", a <= b)
  print(f"{a} == {b}: ", a == b)
  print(f"{a} != {b}: ", a != b)