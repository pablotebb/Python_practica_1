from modulo_decoradores import *

@funcion_d
def una_funcion():
  """
    Función que imprime una función
  """
  print("imprimo desde una función")
  
def suma_dos_valores(num1 = 0, num2 = 0):
  """
    Función que imprime la suma de dos valores recibidos como parámetros
  """
  return (num1 + num2)


def imprime_nombre_y_apellido(nombre, apellidos):
  """
    Función que imprime el nombre y apellidos mandados por parámetros
  """
  print(f"Tu nombre y apellidos son: {nombre} {apellidos}")
  
@funcion_a
def imprime_nombre_con_alias(nombre, apellidos, alias="[No tiene alias]"):
  """
    Función que imprime el nombre, apellidos y alias, recibidos por parámetros. Si no recibe el alias, imprime una cadena por defecto
  """
  print(f"Tu nombre es {nombre} y tus apellidos {apellidos}, y tienes el alias {alias}")
 
@funcion_a 
def imprime_en_mayusculas_cadenas_que_recibe(*cadena):
  """
    Función que imprime en mayusculas los parámetros que recibe
  """
  print(f"cadena, que tiene {cadena} es de tipo: {type(cadena)}")
  for i in cadena:
    print(i.upper())

  
