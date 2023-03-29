def saluda_dos_veces():
  """ 
    Esta función saluda dos veces, usando las comillas simples y las comillas dobles
  """
  print("--------------------------------------")
  print("Hola!")
  print('Hola')
  print("--------------------------------------")
  
def saluda_dos_veces_con_un_parametro(saludo):
  """
    Esta función saluda dos veces, al pasarle un parámetro
  """
  print("--------------------------------------")
  print(saludo)
  print(saludo)
  print("--------------------------------------")
 
  
def saluda_dos_veces_con_dos_parametros(saludo="[falta parámetro 1]", saludo2="[falta parámetro 2]"):
  """ 
    Esta función saluda dos veces, pasándole 2 parámetros
  """
  print("--------------------------------------")
  print(saludo)
  print(saludo2)
  print("--------------------------------------")
    
def devolviendo_tipos():
  '''
    Esta función devuelve los tipos de diversos tipos de objetos
  '''
  print("--------------------------------------")
  print(type("soy un str"))
  print(type(5))
  print(type(1.5))
  print(type(True))
  print(type(3 + 1j))
  print(type(print("esto es una cadena")))
  print("--------------------------------------")
  

  




