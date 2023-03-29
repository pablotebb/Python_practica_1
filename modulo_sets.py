from modulo_decoradores import *

@funcion_d
def creamos_un_set_normal_y_mas():
  """
    Función que crea un set y más
  """
  my_set = {}
  print(f"Este es el set {my_set}, y es de tipo {type(my_set)}")
  my_set = {"uno", "dos", 1, "tres", "uno", 2, 1}
  print(f"Este es el set {my_set}, y es de tipo {type(my_set)}")
 
@funcion_d
def imprime_algunas_funciones_set():
  """
    Función que crea un set y algunas funciones de este set
  """
  my_set = {"uno", "dos", 1, "tres", "uno", 2, 1}
  print("my_set", my_set)
  print("len(my_set)", len(my_set))
  my_set.add("Pepino")
  my_set.add("Pepino")
  print("my_set.add('Pepino')", my_set)
  print("my_set.add('Pepino')", my_set)
  my_set.remove("Pepino")
  print("my_set.remove('Pepino')", my_set)
  my_set.clear()
  print("my_set.clear()", my_set)
  my_set1 = {1, "Ernesto", "tres"}
  my_set2 = {"Juanito", "Pepita", 1}
  print(my_set1.union(my_set2))
  
@funcion_d
def no_se_puede_acceder_a_un_set():
  """
    Función que crea un set y lo muestra, y te demuestra que no puedes acceder al set de determinada forma, porque no esta estructuralmente ordenado
  """
  my_set = {"uno", "dos", 1, "tres", "uno", 2, 1}
  print("my_set", my_set)
  try:
    print(my_set[0])
  except TypeError as error:
    print(f"No se puede acceder a un set, error: {error}")
  finally: 
    my_list = list(my_set)
    print("Si pasamos el set a una lista, si podemos acceder; my_set[0]:", my_list[0])
    
@funcion_a
def busqueda_en_set(nombre):
  """
    Función que busca en un set
  """
  my_set = {"uno", "dos", 1, "tres", "uno", 2, 1}
  print(f"{nombre} in {my_set}:", nombre in my_set)
  
  
@funcion_d
def imprime_todas_funciones_set():
  """ 
    Funcion que crea un set, e imprime todas sus funciones
  """
  my_set = set()
  print(dir(my_set))
  