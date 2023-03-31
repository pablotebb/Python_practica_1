from modulo_decoradores import *
import math


@funcion_d
def name_error():
  """
    Función que al comentar la variable "language" da este error:
    NameError: name 'language' is not defined
  """
  language = "Spanish" # Comentar para ver error
  print(language)
  
@funcion_d
def index_error():
  """
    Función que al descomentar un print da este error:
    IndexError: list index out of range
  """
  my_list = ["Python", "Cobol", "Java", "Javascript", "C++"]
  print(my_list[0])
  print(my_list[4])
  print(my_list[-1])
  # print(my_list[5]) # Descomentar para ver error
  
@funcion_a 
def module_not_found_error():
  """
    Función que al descomentar el import nos devuelve este error:
    ModuleNotFoundError: No module named 'maths'
  """
  # import maths  # Descomentar para ver error
  print("libreria math")
  
  
@funcion_a 
def attribute_error():
  """
    Función que al descomentar el print nos devuelve este error:
    AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
  """
  # print(math.PI) # Descomentar para ver el error
  print("libreria math")
  
@funcion_a 
def import_error():
  """
    Función que al descomentar el import nos muestra este error:
    ImportError: cannot import name 'PI' from 'math' (unknown location)
  """
  # from math import PI # descomentar para ver el error
  print("pi")
  
@funcion_a
def key_error():
  """
    Función que al descomentar el acceso al diccionario, nos devuelve este error:
    KeyError: 'Apelido'
  """
  my_dicc= {"Nombre":"Pepe", "Apellido": "García", "Edad": 35}
  print(my_dicc["Nombre"])
  # print(my_dicc["Apelido"]) # descomentar para ver el error
  
@funcion_a
def type_error():
  """
    Función que al descomentar el print nos devuelve este error:
    TypeError: list indices must be integers or slices, not str
  """
  my_list = ["Python", "Cobol", "Java", "Javascript", "C++"]
  # print(my_list["0"]) # descomentar para ver el error 
  print(my_list[0])
  
@funcion_a 
def value_error():
  """
    Función que al descomentar el valor nos devuelve este error:
    ValueError: invalid literal for int() with base 10: '10 años'
  """
  # my_int = int("10 años") # descomentar para ver el error
  my_int = int("10")
  print(my_int)
  print(type(my_int))
  
@funcion_a
def zero_division_error():
  """
    Función que al descomentar el print nos devuelve este error: 
    ZeroDivisionError: division by zero
  """
  # print(4/0) # descomentar para ver el error
  print(4/2)
  

  
  