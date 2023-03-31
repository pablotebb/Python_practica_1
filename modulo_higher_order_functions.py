from modulo_decoradores import *

def suma_1(num1):
  return num1 + 1

def suma_2(num2):
  return num2 + 5

@funcion_a
def suma_valores(num1, num2, f_suma):
  print(f_suma(num1 + num2))
  
  
### Closures ###

def sum_1(num1):
  print(f"num1 es: {num1}")
  def sum_2(num2):
    print(f"num1 es: {num2}")
    return num2 + 10 + num1
  return sum_2



def multiplica(listado):
  return 2 * listado


def filtar_numero_mas_grandes_que_diez(num):
  if num > 10:
    return True
  return False

def sumar_dos_valores_dados(num1, num2):
  return num1 + num2



