from modulo_decoradores import *

@funcion_d
def declara_una_lista_con_corchetes():
  """
    Declara una lista con corchetes, la usa, la modifica y la usa otra vez
  """
  mi_lista = []
  print(f"Mi lista {mi_lista} es de tipo: {type(mi_lista)}")
  mi_lista = [35, 24, 343, 33, 67, 98, 33]
  print(f"Mi lista {mi_lista} es de tipo: {type(mi_lista)}")
  print("mi_lista[0]", mi_lista[0])
  print("mi_lista[1]", mi_lista[1])
  print("mi_lista[-1]", mi_lista[-1]) 
  print("mi_lista[-4]", mi_lista[-4])
  print("mi_lista.count(33)", mi_lista.count(33))
  print("mi_lista.index(33)", mi_lista.index(33))
  
@funcion_d
def declara_una_lista_con_nombre():
  """
    Declara una lista con nombre, la usa, la modifica y la usa otra vez
  """
  mi_lista = list()
  print(f"Mi lista {mi_lista} es de tipo: {type(mi_lista)}")
  mi_lista = [33, 23.45, "Pepe", "Lopez", "Pepe"]
  print(f"Mi lista {mi_lista} es de tipo: {type(mi_lista)}")
  print("mi_lista[0]", mi_lista[0])
  print("mi_lista[1]", mi_lista[1])
  print("mi_lista[-1]", mi_lista[-1]) 
  print("mi_lista[-4]", mi_lista[-4])
  print("mi_lista.count('Pepe')", mi_lista.count("Pepe"))
  print("mi_lista.index('Pepe')", mi_lista.index('Pepe'))
  
  
@funcion_d
def desempaqueta_una_lista():
  """
    funcion que desempaqueta una lista
  """
  mi_lista = ["Pepe", "Dorta", 35, "Calle de la Noria, 34"]
  nombre, apellido, edad, calle = mi_lista
  print(f"Hola {nombre} {apellido} tienes {edad} años y vives en {calle}")
  
@funcion_d
def concatena_dos_cadenas():
  """
    función que concatena dos listas
  """
  lista_uno = ["Pepe", "Dorta", 35, "Calle de la Noria, 34"]
  lista_dos = ["Pepe", "Fernandez", 67, ("calle", "teléfono", "dirección")]
  print(lista_uno + lista_dos)
  
@funcion_d
def algunas_funciones_cadenas_dos():
  """
    función que usa algunas funciones de listas
  """
  mi_lista = ["Pepe", "Dorta", 35, "Calle de la Noria, 34"]
  print("mi_lista = ", mi_lista)
  mi_lista.append("Dorta")
  print("mi_lista.append('Dorta')", mi_lista)
  mi_lista.insert(1, "Fernandez")
  print("mi_lista.insert(1, 'Fernandez')", mi_lista)
  mi_lista[1] = "Rojo"
  print(" mi_lista[1] = 'Rojo'", mi_lista)
  mi_lista.remove("Rojo")
  print("mi_lista.remove('Rojo')", mi_lista)
  mi_lista.remove(35)
  print("mi_lista.remove(35)", mi_lista)
  dato = mi_lista.pop()
  print("dato = mi_lista.pop()", mi_lista)
  print(dato)
  dato = mi_lista.pop(2)
  print("dato = mi_lista.pop(2)", mi_lista)
  print(dato)
  copia = mi_lista.copy()
  print("copia = mi_lista.copy()", copia)
  del mi_lista[1]
  print("del mi_lista[1]", mi_lista)
  print("copia = ", copia)
  mi_lista.clear()
  print("mi_lista.clear()", mi_lista)
  print("copia = ", copia)
  copia.reverse()
  print("copia.reverse()", copia)
  copia.sort()
  print("copia.sort()", copia)
  copia.sort(reverse=True)
  print("copia.sort(reverse=True)", copia)
  
@funcion_d
def porciones_lista():
  """
    Muestra porciones de una lista
  """
  lista = ["Benito Lopez", "Juan Díaz", "Ernesto Pérez", "Juan Díaz"]
  print("lista = ", lista)
  print("lista[1:3]", lista[1:3])

@funcion_d
def devuelve_todas_funciones_lista():
  """
    Devuelve todos las funciones de una lista
  """
  lista = [1,2,5,8,2]
  print("lista = ", lista)
  print(dir(lista))