from modulo_decoradores import *
import xml 
import csv 
import json 
import os 

@funcion_a
def abre_archivo():
  """
    Función que abre archivo, escribe datos y los lee 
  """
  try:
    txt_file = open("./my_file.txt", "w+")
    txt_file.write("Mi nombre es Palito\n Mi apellido es Palotes\n tengo 35 años\n y mi lenguaje preferido es Python")
    txt_file.seek(0)
    print("+++++++++++++++++")
    print(txt_file.read(10))
    print("+++++++++++++++++")
    print(txt_file.readline())
    print(txt_file.readline())
    print("+++++++++++++++++")
    txt_file.seek(0)
    for line in txt_file.readlines():
      print(line)
    print("+++++++++++++++++")
    txt_file.close()
  except:
    print("No se pudo leer el archivo")
    
@funcion_a
def leer_archivo():
  """
    Función que abre un archivo y lo lee
  """
  txt_file = open("./my_file.txt", "r")
  print(txt_file.read())
  txt_file.seek(0)
  print("********************")
  print(txt_file.readline())
  print(txt_file.readline())
  print("********************")
  
@funcion_a 
def agregar_archivo():
  """
    Función que abre un archivo y agrega un datos y los lee
  """
  try:
    with open("./my_file.txt", "a+") as txt_file:
      txt_file.write("\n Esto va al final del texto")
      txt_file.seek(0)
      print(txt_file.read())
  except:
    print("Error en el archivo")
 
