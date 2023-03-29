from modulo_decoradores import *

def condicional_devuelve(my_condition):
  """
    función que devuelve una cosa u otra, dependiendo del argumento recibe
  """
  print("--------------------------------------")
  if my_condition:
    return "Se ejecuta la condición del if"
  
  return "No se ejecuta la condición del if"

@funcion_a
def evalua_un_numero(numero):
  """
    Función que evalua un número e imprime respuesta según el número
  """
  if numero > 10 and numero < 20:
    print("Es mayor que 10 y menor que 20")
  elif numero == 25:
    print("Es igual que 25")
  else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
    
  print("Se ejecuta continua")
  
@funcion_a
def dame_tu_nombre(dato = ""):
  """
    Función que si no le das el argumento te devuelve un mensaje, y si se lo das te devuelve otros mensajes
  """
  if not dato:
    print("no me distes el nombre")
    
  if dato == "Pablo":
    print("Hola Pablo")
  else:
    print("Hola amigo")