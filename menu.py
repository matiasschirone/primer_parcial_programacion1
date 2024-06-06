

def validar_entero(numero):
    """La función "validar_entero" comprueba si una entrada determinada es un número entero válido.

    Args:
        numero (_type_): El parámetro "numero" es una variable que representa un valor que queremos comprobar

    Returns:
        _type_: La función devuelve un valor booleano. Devuelve "Verdadero" si la entrada "numero" se puede convertir a un número entero y "Falso" en caso contrario.
    """

    try:
        int(numero)
        return True
    except ValueError:
        return False



def menu()->str:
    """
    Muestra un menú de opciones y solicita al usuario que ingrese una opción.

    Returns:
        str: La opción seleccionada por el usuario. 
    """
    limpiar_pantalla()
    print(f"{'menu de opciones':^50s}")
    print("1- Catgar archivos .CSV")
    print("2- Imprimir lista")
    print("3- Asignar Rating")
    print("4. Asignar genero")
    print("5- filtrar por genero")
    print("6- Ordenar peliculas")
    print("7- Informar Mejor Rating")
    print("8- Guardar peliculas")
    print("9- Salir")
    
    opcion = input("Por favor, ingrese el número de la opción elegida: ")

    if validar_entero(opcion):
        return int(opcion)
    else:
        return False
     
    
def pausar():
    """
    Pausa la ejecución del programa hasta que el usuario presione una tecla.
    """
    import os
    os.system("pause")
    
def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    import os
    os.system("cls")