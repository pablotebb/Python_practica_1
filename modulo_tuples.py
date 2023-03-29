from modulo_decoradores import *

@funcion_d
def declara_tuple_forma_normal_y_mas():
  """
    Funcion que declara una tupla de manera normal y...
  """
  my_tuple = ()
  print(f"La tupla {my_tuple} es del tipo {type(my_tuple)}")
  my_tuple = (34, "John", "Gonzalvez", "Calle de la Pera")
  print(f"La tupla {my_tuple} es del tipo {type(my_tuple)}")
  
@funcion_d
def declara_tuple_forma_con_nombre_y_mas():
  """
    Funcion que declara una tupla mediante su palabra reservada y...
  """
  my_tuple = tuple()
  print(f"La tupla {my_tuple} es del tipo {type(my_tuple)}")
  my_tuple = (34, "John", "Gonzalvez", "Calle de la Pera")
  print(f"La tupla {my_tuple} es del tipo {type(my_tuple)}")

@funcion_d
def tuplas_son_inmutables():
  """
    funcion que demuestra que las tuplas son inmutables
  """
  my_tuple = (34, "John", "Gonzalvez", "Calle de la Pera")
  try:
    my_tuple[0] = "Pepe"
    print(f"Esta orden no se ejecuta, y esta es la tupla: {my_tuple}")
  except TypeError as error:
    print(f"Ha habido un error: {error}")
    
@funcion_d
def accedemos_a_las_tuplas():
  """
    función por el cual accedemos a algunos elementos de la misma
  """
  my_tuple = (34, "John", "Gonzalvez", "Calle de la Pera")
  print("my_tuple", my_tuple)
  print("my_tuple[0]", my_tuple[0])
  print("my_tuple[-1]", my_tuple[-1])
  
@funcion_d
def algunas_funciones_tuple():
  """
    función que imprime algunas funciones de tupla 
  """
  my_tuple = (34, "John", "Gonzalvez", "Calle de la Pera", "John")
  print("my_tuple", my_tuple)
  print("my_tuple.count('John')", my_tuple.count("John"))
  print("my_tuple.index('John')", my_tuple.index("John"))
  print("my_tuple.index('Gonzalvez')", my_tuple.index("Gonzalvez"))
  my_tuple.insert(0, "Pepe")
  print(" my_tuple.insert(0, 'Pepe')", my_tuple)


@funcion_a
def pasar_de_tuple_a_list(tupla):
  """
    función que te pasa de una tuple a una list, y usa alguno de sus métodos, y luego lo pasa a tuple y lo devuelve
  """
  lista = list(tupla)
  lista.insert(0, "Pepe")
  tupla2 = tuple(lista)
  print("--------------------------------------")
  return tupla2

@funcion_d
def todas_funciones_tuple():
  """
    función que devuelve todas las funciones de una tupla
  """
  my_tuple = (34, "John", "Gonzalvez", "Calle de la Pera", "John")
  print(dir(my_tuple))
  


  