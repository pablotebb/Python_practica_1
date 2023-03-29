
def muestra_variables():
  """
    Función que muestra variables de distintos tipos 
  """
  my_string_variable = "Mi string variable"
  my_int_variable = 5
  my_bool_variable = True
  print("--------------------------------------")
  print(my_string_variable)
  print(my_int_variable)
  print(my_bool_variable)
  print("--------------------------------------")
  
def muestra_variables_por_parametros(variable1="[falta variable1]", variable2="[falta variable2]"):
  """
    Función que muestra variables que son mandadas por parametros
  """
  print("--------------------------------------")
  print(variable1)
  print(variable2)
  print("--------------------------------------")
  
def concatena_cadenas():
  """ 
    Esta función concatena cadenas
  """
  print("--------------------------------------")
  print("Hola", "Juan", "María", "Pepe")
  print("Hola amigos, como están", "tontitos!")
  print("--------------------------------------")
  
def longitud_cadena(cadena=""):
  """
    Función que imprime la longitud de una cadena
  """
  cadena2 = len(cadena)
  print("--------------------------------------")
  print(f"La longitud de la cadena {cadena} es: {cadena2}")
  print("--------------------------------------")
  
def practicando_con_variables_en_linea():
  """
    Función que distribuye variables entre variables y las ejecuta
  """
  nombre, apellido, edad, alias = "Juan", "Mendez", 35, "Campeón"
  print("--------------------------------------")
  print(f"Hola {nombre} {apellido} tu edad es: {edad} y te apodas: {alias}")
  print("--------------------------------------")
  
def practicando_con_variables_en_linea_devolviendo(nombre="[desconocido]", apellido="[desconocido]", edad="[desconocido]", alias="[desconocido]"):
  """
    Función que recibe parámetros y los muestra en una cadena
  """
  print("--------------------------------------")
  return f"Hola {nombre} {apellido} tu edad es: {edad} y te apodas: {alias}"
  print("--------------------------------------")
  
def pregunta_y_da_respuesta():
  """ 
    Función que te pide el nombre y la edad, y te las imprime en pantalla
  """
  nombre = input('¿Cual es tu nombre? ')
  edad = input('¿Cual es tu edad? ')
  if nombre !="" and edad != "":
    print("--------------------------------------")
    print(f"Hola {nombre}, tienes: {edad} años")
    a_variable = nombre
    nombre = edad
    edad = a_variable
    print(f"Hola {nombre}, tienes: {edad} años")
    print("--------------------------------------")
  else:
    print("--------------------------------------")
    print("Debes ingresar los 2 datos!!")
    print("--------------------------------------")
    
def forzando_el_tipo():
  """
    función que demuestra el prototipado dinámico de Python 
  """
  mi_cadena = "Hola mundo"
  mi_cadena = 5 
  mi_cadena = 5.6
  print("--------------------------------------")
  print(type(mi_cadena))
  print("--------------------------------------")
    
  