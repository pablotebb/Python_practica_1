from modulo_decoradores import *

@funcion_a
def suma_dos_numeros(num1 = 0, num2 = 0):
  """
    Función que suma 2 números y si detecta error lanza una exepción
  """
  try:
    print(num1 + num2)
    print("se ejecuta despues de la suma y no cuando hay una exepción")
  except: 
    print("Se ha producido una exepción") 
    
@funcion_a
def suma_dos_numeros_2(num1 = 0, num2 = 0):
  """
    Función que suma 2 números y si detecta error lanza una exepción y otras cosas
  """
  try:
    print(num1 + num2)
    print("No se ha producido un error")
  except:
    print("Se ha producido un error")
  else: 
    print("Se ejecuta si no se produce una excepción")
  finally:
    print("Se ejecuta siempre")
    
@funcion_a
def suma_dos_numeros_3(num1 = 0, num2 = 0):
  """
    Función que suma dos numeros y detecta si hay un tipo de error...
  """
  try:
    print(num1 + num2)
    print("No se ha producido un error")
  except ValueError:
    print("Se ha producido un error ValueError")
  except TypeError:
    print("Se ha producido un TypeError")
    
@funcion_a
def suma_dos_numeros_4(num1, num2):
  """
    Función que suma 2 números y si detecta un error lanza varias errores...
  """
  try:
    print(num1 + num2)
    print("No se ha producido un Error")
  except ValueError as error:
    print(error)
  except Exception as error2:
    print(error2)