def funcion_a(funcion_b):
    """
      Función decoradora que recibe 2 parámetros
    """
    def funcion_c(*num):
        print("--------------------------------------")
        funcion_b(*num)
        print("--------------------------------------")

    return funcion_c
  
def funcion_d(funcion_b):
    """
      Función decoradora que no recibe parámetros
    """
    def funcion_c():
        print("--------------------------------------")
        funcion_b()
        print("--------------------------------------")

    return funcion_c