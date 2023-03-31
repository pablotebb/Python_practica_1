from modulo_decoradores import *

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime 

@funcion_a
def imprime_fecha_hora_sellotiempo(date:datetime):
  """
    Función que imprime distintos métodos de tiempo 
  """
  # Fecha
  print(date.year)
  print(date.month)
  print(date.day)
  # Hora 
  print(date.hour)
  print(date.minute)
  print(date.second)
  # Sello de tiempo 
  print(date.timestamp())
  
@funcion_a
def imprime_fecha(date:datetime):
  """
    Función que imprime fecha 
  """
  print(f"Fecha de hoy: {date.day}/{date.month}/{date.year}")
  
@funcion_a 
def imprime_hora(date:datetime):
  """
    Función que imprime la hora
  """
  print(f"Reloj: {date.hour}:{date.minute}:{date.second}")
  
@funcion_a
def imprime_sello_tiempo(date:datetime):
  """
    Función que imprime sello de tiempo
  """
  print(f"Sello de tiempo: {date.timestamp()}")
  
@funcion_a
def imprime_fecha_que_damos(year = 0000, month = 00, day = 00):
  """
    Función que imprime la fecha que le damos  
  """
  try:
    print(datetime(year, month, day))
  except: 
    print("Has entrado mal los datos")
    
@funcion_a 
def imprime_hora_que_damos(hour = 00, minute = 00, second = 0):
  """
    Función que imprime la hora que le damos
  """
  try:
    print(time(hour, minute, second))
  except:
    print("Has entrado mal los datos")
    
@funcion_d
def imprime_fecha_de_hoy():
  """
    Función que imprime la fecha de hoy 
  """
  try:
    print(date.today())
  except: 
    print("Has entrado mal los datos")
    
@funcion_a
def imprime_fecha_que_damos(year, month, day):
  """
    Fecha que nos devuelve la fecha que le damos 
  """    
  try:
    print(f"{date(year, month, day)}")
  except:
    print("Has entrado mal los datos")
    
@funcion_d 
def suma_resta_tiempos():
  """
    Función que suma y resta dos tiempos
  """
  start_time = timedelta(200, 100, 100)
  end_time = timedelta(300, 100, 100)
  
  print("start_time:", start_time)
  print("end_time:", end_time)  
  print("end_time - start_time:", end_time - start_time)
  print("end_time + start_time:", end_time + start_time)