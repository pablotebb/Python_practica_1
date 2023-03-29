from modulo_decoradores import *

@funcion_a
def cumple_perro(edad = 100):
  """
    Función que evalua la edad de un perro y da una felicitación
  """
  while edad <= 5:
    print("Feliz cumpleaños joven perrito!!!")
    edad += 1
  else:
    print("Esto siempre se ejecuta, sea el perro joven (<=5) o viejo (>=6)")
    print("Todos los perros (jovenes y viejos) son increibles!!")
    
@funcion_a
def cumple_persona(edad = 130):
  """
    Función que evalua la edad de una persona y da una felicitación
  """
  numeroveces = 1
  while edad < 41:
    print("Feliz cumpleaños jovencito!!!")
    if numeroveces  == 1:
      break
    edad += 1
  else:
    print("Todos las persona (viejas) son increibles!!")
    
@funcion_a
def imprime_lista_y_pasa_a_otras_estructuras_e_imprime(p_lista):
  """
    Función que recibe una lista, e imprime los elementos en lista, tupla, diccionario y set
  """
  p_tuple = tuple(p_lista)
  p_set = set(p_lista)
  p_dicc = {
    "nombre": p_lista[0],
    "apellidos": p_lista[1],
    "edad": p_lista[2],
    "calle": p_lista[3]
  }
  print("\nLista:")
  for i in p_lista:
    print(i)
    
  print("\nTupla:")
  for i in p_tuple:
    print(i)
    
  print("\nSet:")
  for i in p_set:
    print(i)
    
  print("\nDiccionario:")
  for i in p_dicc:
    print(p_dicc[i])
    
@funcion_d
def imprime_todos_campos_diccionario_menos_edad():
  """
    Funcion que crea un diccionario, lo imprime e imprime todos los campos menos la edad
  """
  p_dicc = {
    "nombre": "Pepe",
    "apellidos": "Lopez Gamez",
    "edad": 35,
    "calle": "Calle de Ramonal"
  }
  
  print("\nDiccionario:")
  print(p_dicc)
  print("\nDiccionario menos edad:")
  for i in p_dicc:
    if(i == "edad"):
      continue
    print(f"{i}:", p_dicc[i])
    

  
  
  