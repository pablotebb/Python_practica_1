# import modulo_hello
# from modulo_hello import saluda_dos_veces, saluda_dos_veces_con_un_parametro
from modulo_hello import *
from modulo_variables import *
from modulo_operators import *
from modulo_strings import *
from modulo_lists import *
from modulo_tuples import *
from modulo_sets import *
from modulo_dicts import *
from modulo_conditionals import *
from modulo_loops import *
from modulo_functions import *
from modulo_clases import *
from modulo_exeptions import *
from modulo_modules import *
from modulo_dates import *
from modulo_list_comprehension import *
from modulo_lambdas import *
from modulo_higher_order_functions import *
from modulo_errors import *
from modulo_file_handling import *
from functools import reduce 
import datetime



# MODULO HELLO

# modulo_hello.saluda_dos_veces()

saluda_dos_veces()

try:
  saluda_dos_veces_con_un_parametro("Hola Juan")
except:
  print("Ha habido algún error!!!")
  
saluda_dos_veces_con_dos_parametros()

saluda_dos_veces_con_dos_parametros("Hola Ernesto")

saluda_dos_veces_con_dos_parametros(saludo2="Hola Ernesto")
  
saluda_dos_veces_con_dos_parametros("Hola Rosa", "Hola Pepe")

devolviendo_tipos()

# MODULO VARIABLES

muestra_variables()

muestra_variables_por_parametros("Hola Juan", "Hola María")

concatena_cadenas()

longitud_cadena("Benito Fernandez Lopez")

practicando_con_variables_en_linea()

print(practicando_con_variables_en_linea_devolviendo())

print(practicando_con_variables_en_linea_devolviendo("Juan", "Bencomo", 45, "El guanche"))

# pregunta_y_da_respuesta()

forzando_el_tipo()

# MODULO OPERATORS

suma(3, 4)

resta(3, 4)

multiplicacion(3, 4)

division_decimal(3, 4)

division_entera(3, 4)

modulo(3, 4)

imprime_cadena_con_numero()

imprime_cadena_tantas_veces()

imprime_operaciones_con_enteros(3, 4)

imprime_operaciones_con_enteros(4, 3)

imprime_operaciones_con_enteros(4, 4)

# MODULO STRINGS

imprime_longitud_dos_cadenas_y_concatena("Hola amigo", "¿como estás?")

usando_saltos_tabuladores_etc()

print_formateos()

print_formateos("Pepe", "Perez", 35)

desempaquetado_caracteres()

desempaquetado_caracteres("Pablo")

slice_cadena()

algunas_funciones_cadenas()

algunas_funciones_cadenas("pablo")

algunas_funciones_cadenas("python")

algunas_funciones_cadenas("Python")

todas_funciones_cadenas()

# MODULO LISTS

declara_una_lista_con_corchetes()

declara_una_lista_con_nombre()

desempaqueta_una_lista()

concatena_dos_cadenas()

algunas_funciones_cadenas_dos()

porciones_lista()

devuelve_todas_funciones_lista()

# MODULO TUPLES

declara_tuple_forma_normal_y_mas()

declara_tuple_forma_con_nombre_y_mas()

tuplas_son_inmutables()

accedemos_a_las_tuplas()

# algunas_funciones_tuple()

una_tupla = (3, "Lopez", "Jose", 32.5)

tupla_vuelta = pasar_de_tuple_a_list(una_tupla)

print("pasar_de_tuple_a_list(una_tupla)", tupla_vuelta)

print("--------------------------------------")

todas_funciones_tuple()

# MODULO SETS
creamos_un_set_normal_y_mas()

imprime_algunas_funciones_set()

no_se_puede_acceder_a_un_set()

busqueda_en_set("tres")

busqueda_en_set("caca")

imprime_todas_funciones_set()

# MODULO DICTS

creamos_un_dict_normal_y_mas()

creamos_un_dict_con_nombre_y_mas()

my_dict = {
    "nombre": "Pepe",
    "apellidos": "López García",
    "edad": 45,
    1: "Diseñador"
  }

accedemos_a_dict(my_dict)

algunas_funciones_dict()

todas_funciones_dict()

# MODULO CONDITIONALS

print(condicional_devuelve(False))
print("--------------------------------------")
respuesta = condicional_devuelve(True)
print(respuesta)
print("--------------------------------------")

evalua_un_numero(5)
evalua_un_numero(25)
evalua_un_numero(26)
evalua_un_numero(12)

# 
# nombre = input("Cual es tu nombre? ")
# dame_tu_nombre(nombre)

entrar = False

# try: 
#   edad = int(input("Dame la edad de tu perro si es joven y cumple hoy años: "))
#   entrar = True
# except ValueError:
#   print("Debes de entrar la edad")

# cumple_perro()

# if entrar:
#   cumple_perro(edad)
  
  
# try: 
#   edad = int(input("Dame tu edad si eres joven y cumple hoy años: "))
#   entrar = True
# except ValueError:
#   print("Debes de entrar la edad")
  
# if entrar:
#   cumple_persona(edad)
  
imprime_lista_y_pasa_a_otras_estructuras_e_imprime(["Pepe", "Hernandez Perez", 35, "Calle del Escabonal"])

imprime_todos_campos_diccionario_menos_edad()

# MODULO FUNCTIONS

una_funcion()

una_funcion()

una_funcion()

solucion = suma_dos_valores(2, 7)
solucion2 = suma_dos_valores(2.34, 7.23)
solucion3 = suma_dos_valores("2", "7")
print("--------------------------------------")
print(solucion)
print("--------------------------------------")
print(solucion2)
print("--------------------------------------")
print(solucion3)
print("--------------------------------------")

imprime_nombre_y_apellido("Juan", "Rodríguez Fraga")

imprime_nombre_y_apellido(apellidos = "Lopez Alegría", nombre = "Ernesto")

print("--------------------------------------")

imprime_nombre_con_alias("Juan", "Oramas Jimenez")

imprime_nombre_con_alias("Perico", "Delgado Sánchez", "El chapucero")

imprime_en_mayusculas_cadenas_que_recibe("Juani", "Alberto", "Ani")

imprime_en_mayusculas_cadenas_que_recibe("Petra")


# MODULO CLASES 

print("--------------------------------------")
print(ClaseVacia)
print("--------------------------------------")

print("--------------------------------------")
print(ClaseVacia()) 
print("--------------------------------------")

objeto_clase = ClaseVacia()

print("--------------------------------------")
print(objeto_clase)
print("--------------------------------------")


super = Super("Hiperdino")
super.agregar_articulo("Queso", 1)
super.agregar_articulo("Leche", 2)
super.agregar_articulo("Yogours", 8)
super.agregar_articulo("Vino", 1)
super.get_listado()


# MODULO EXEPTIONS

suma_dos_numeros(2, 3)

suma_dos_numeros(2, "3")

suma_dos_numeros_2(2, 3)

suma_dos_numeros_2(2, "3")

suma_dos_numeros_3(4, 5)

suma_dos_numeros_3(4, "5")

suma_dos_numeros_3(4, "hola")

suma_dos_numeros_4(3, 7)

suma_dos_numeros_4(3, "7")


# MODULO MODULES  

imprime_numero_pi()

imprime_numero_pi_con_errors()

imprime_numero_pi_2()

imprime_valor_desde_modulo("Hola")

imprime_valor_desde_modulo(3)

imprime_valor_desde_un_modulo_2("Holita")

imprime_valor_desde_un_modulo_2(4)

suma_tres_valores_desde_un_modulo(1, 2, 3)

suma_tres_valores_desde_un_modulo_2(4, 5, 6)

# MODULO DATES 
now = datetime.datetime.now()

imprime_fecha_hora_sellotiempo(now)

imprime_fecha(now)

imprime_hora(now)

imprime_sello_tiempo(now)

imprime_fecha_que_damos(2022, 3, 31)

imprime_hora_que_damos(15, 3, 13)

imprime_fecha_de_hoy()

imprime_fecha_que_damos(2000, 1, 31)

suma_resta_tiempos()

imprime_una_lista()

imprime_rango_de_ocho_elementos()

imprime_rango_de_ocho_elementos_2()

# MODULO modulo_lambdas

print("--------------------------------------")

print(suma_tres_valores(5)(2, 4))

print("--------------------------------------")

# MODULO modulo_higher_order_funciones 

suma_valores(5, 2, suma_1)

suma_valores(5, 2, suma_2)

sum_closure = sum_1(1)
print(sum_closure(5))

print(sum_1(10)(3))

# Map

listado = [2, 5, 3, 15, 12, 11, 19, 23]

print("--------------------------------------")
print(listado)
print("--------------------------------------")

print("--------------------------------------")
print(list(map(multiplica, listado)))
print("--------------------------------------")

print("--------------------------------------")
print(list(map(lambda x: x * 2, listado)))
print("--------------------------------------")

# Filter 

print("--------------------------------------")
print(list(filter(filtar_numero_mas_grandes_que_diez, listado)))
print("--------------------------------------")

print("--------------------------------------")
print(list(filter(lambda x: x > 10, listado)))
print("--------------------------------------")

# Reduce 
print("--------------------------------------")
print(reduce(sumar_dos_valores_dados, listado))
print("--------------------------------------")

# MODULO modulo_errors

name_error()

index_error()

module_not_found_error()

attribute_error()

key_error()

type_error()

import_error()

value_error()

zero_division_error()

# MODULO modulo_file_handling

abre_archivo()

leer_archivo()

agregar_archivo()