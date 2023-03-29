from modulo_decoradores import *

@funcion_d
def creamos_un_dict_normal_y_mas():
  """
    Función que declara un diccionario, te dice el tipo, te mide el diccionario, etc...
  """
  my_dict = {}
  print(f"Este es mi diccionario {my_dict} y es de tipo {type(my_dict)}")
  print(f"y mide {len(my_dict)}")
  my_dict = {
    "nombre": "Pepe",
    "apellidos": "López García",
    "edad": 45,
    1: "Diseñador"
  }
  print(f"Este es mi diccionario {my_dict} y es de tipo {type(my_dict)}")
  print(f"y mide {len(my_dict)}")
  

@funcion_d
def creamos_un_dict_con_nombre_y_mas():
  """
    Función que crea un diccionario mediante una clase y más cosas...
  """
  my_dict = dict()
  print(f"Este es mi diccionario {my_dict} y es de tipo {type(my_dict)}")
  print(f"y mide {len(my_dict)}")
  my_dict = {
    "nombre": "Pepe",
    "apellidos": "López García",
    "edad": 45,
    1: "Diseñador"
  }
  print(f"Este es mi diccionario {my_dict} y es de tipo {type(my_dict)}")
  print(f"y mide {len(my_dict)}")
  
@funcion_a
def accedemos_a_dict(dicc):
  """
    Función que muestra las formas de acceder a un diccionio
  """
  print("dicc[0]", dicc["nombre"])
  print("dicc[0]", dicc["edad"])
  print(f"'nombre' in {dicc}", "nombre" in dicc)
  print(f"'edad' in {dicc}", "edad" in dicc)
  print(f"'diploma' in {dicc}", "diploma" in dicc)
  
@funcion_d
def algunas_funciones_dict():
  """
    Función que crea un dicionario y le aplica algunas funciones
  """
  my_dict = {
    "nombre": "Pepe",
    "apellidos": "López García",
    "edad": 45,
    1: "Diseñador"
  }
  print("my_dict", my_dict)
  print("my_dict.items()", my_dict.items())
  print("my_dict.keys()", my_dict.keys())
  print("my_dict.values()", my_dict.values())
  print("type(my_dict.items())", type(my_dict.items()))
  print("type(my_dict.keys())", type(my_dict.keys()))
  print("type(my_dict.values())", type(my_dict.values()))
  copia_estructura = dict.fromkeys((my_dict))
  print("dict.fromkeys((my_dict))", dict.fromkeys((my_dict)))
  print("Copia de la estructura del diccionario", copia_estructura)
  
@funcion_d
def todas_funciones_dict():
  """
    Función que crea un diccionario y muestra todas sus funciones
  """
  my_dict = {
    "nombre": "Pepe",
    "apellidos": "López García",
    "edad": 45,
    1: "Diseñador"
  }
  print(dir(my_dict))