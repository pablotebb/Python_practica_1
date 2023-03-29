from modulo_decoradores import *

@funcion_a
def imprime_longitud_dos_cadenas_y_concatena(cadena1, cadena2):
  """
    Función que imprime la longitud de dos cadenas y la imprime 2 veces concatenadas
  """
  print(len(cadena1))
  print(len(cadena2))
  print(cadena1 + " " + cadena2)
  print(f"{cadena1} {cadena2}")
  
@funcion_d
def usando_saltos_tabuladores_etc():
  """
    Función que imprime tabulación, nueva línea, escapado
  """
  nueva_linea = "Este es un string\n con salto de linea"
  tab_linea = "\t Este es un string con tabulacion"
  escape_linea = "\\t Este es un String \\n escapado"
  print(nueva_linea)
  print(tab_linea)
  print(escape_linea)
  
@funcion_a
def print_formateos(nombre="[desconocido]", apellido="[desconocido]", edad=0):
  """ 
    Función que te muestra algunos de los tipos de formateos de una cadena
  """
  print("Tu nombre es {} {} y tu edad es {}".format(nombre, apellido, edad))
  print("Tu nombre es %s %s y tu edad es %d" % (nombre, apellido, edad))
  print("Tu nombre es", nombre, apellido, "y tu edad es", edad)
  print("Tu nombre es " + nombre + " " + apellido + " y tu edad es " + str(edad))
  print(f"Tu nombre es {nombre} {apellido} y tu edad es {edad}")
  
@funcion_a
def desempaquetado_caracteres(cadena="     "):
  """
    función que desempaqueta una cadena de caracteres
  """
  a, b, c, d, e = cadena 
  print(a)
  print(b)
  
@funcion_d
def slice_cadena():
  """
    función que trozea una cadena 
  """
  cadena = "Python"
  print(f"cadena: {cadena}")
  print(f"cadena[1:3]: {cadena[1:3]}")
  print(f"cadena[1:]: {cadena[1:]}")
  print(f"cadena[-2]: {cadena[-2]}")
  print(f"cadena[0:6:2]: {cadena[0:6:2]}")
  print(f"cadena[::-1]: {cadena[::-1]}")
  
@funcion_a
def algunas_funciones_cadenas(cadena= ""):
  """
    algunas funciones de cadenas
  """
  print("cadena.capitalize()", cadena.capitalize())
  print("cadena.upper()", cadena.upper())
  print("cadena.count('t')", cadena.count("t"))
  print("cadena.isnumeric()", cadena.isnumeric())
  print("'1'.isnumeric()", "1".isnumeric())
  print("cadena.lower()", cadena.lower())
  print("cadena.lower().isupper()", cadena.lower().isupper())
  print("cadena.startswith('Py')", cadena.startswith("Py"))
  
@funcion_d
def todas_funciones_cadenas():
  """
    Imprime en pantalla, todas las funciones de las cadenas
  """
  print(dir("hola"))
  
  
