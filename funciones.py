
import random

import json

def get_path_actual(nombre_archivo: str)-> str:
    """Devuelve la ruta completa del archivo proporcionado.


    Args:
        nombre_archivo (str): El nombre del archivo

    Returns:
        str: La ruta completa del archivo.
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def cargar_csv()-> list:
    """Carga los datos de un archivo CSV de películas y los devuelve como una lista de diccionarios.

    Returns:
        list: Lista de diccionarios que representan películas.
    """
    with open(get_path_actual("movies.csv"), "r", encoding="utf-8")as archivo:
        lista_peliculas = []
        encabezado = archivo.readline().strip("\n").split(",")
        
        for linea in archivo.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
    
            id, titulo, genero, rating = linea
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = float(rating)
            lista_peliculas.append(pelicula)
            
    return lista_peliculas
            

def imprimir_lista(lista_peliculas: list)->None:
    """Imprime una lista de películas.

    Args:
        lista_peliculas (list): Lista de diccionarios de las peliculas.
    """
    tam = len(lista_peliculas)
    print("       ****Listado de peliculas****")
    print(f"{'ID':<5} {'Titulo':<30} {'Genero':<15} {'Rating':<6}")
    print("---------------------------------------------------------------")
    for i in range(tam):
        mostrar_pelicula_item(lista_peliculas[i])
    print()
    
def mostrar_pelicula_item(pelicula: dict)->None:
    print(f"{pelicula['id']:<5} {pelicula['titulo']:<30} {pelicula['genero']:<15} {pelicula['rating']:<6}")

def mapear_peliculas(mapeadora, lista: list)->list:
    """va recibiendo cada uno de los elementos de la lista original, y lo que devuelva es lo que va a ir la listaa destino. (devuelve una lista nueva)

    Args:
        mapeadora (function): funcion 
        lista (list): lista original

    Returns:
        list: lista que retorna
    """
    lista_retorno = []
    
    for el in lista:
        lista_retorno.append(mapeadora(el))
        
    return lista_retorno

def rating_random(pelicula: dict)-> dict:
    """Asigna un rating aleatorio entre 1.0 y 10.0 con un decimal a una película.

    Args:
        pelicula (dict): Diccionario que representa una película.

    Returns:
        dict: Diccionario de la película con el rating asignado.
    """
    parte_entera = random.randint(1, 10)
    parte_decimal = random.randint(0, 9)
    rating = float(f"{parte_entera}.{parte_decimal}")
    pelicula['rating'] = rating
    return pelicula
  
def asignar_genero(pelicula: dict)->dict:
    """Asigna un género aleatorio a una película.

    Args:
        pelicula (dict): Diccionario que representa una película.

    Returns:
        dict: Diccionario de la película con el género asignado.
    """
    generos = {1: "drama", 2: "comedia", 3: "acción", 4: "terror"}
    genero_random = random.randint(1, 4)
    pelicula['genero'] = generos[genero_random]
    return pelicula

def filtrar_peliculas_genero(lista: list, genero: str) -> list:
    """Filtra las películas por género.

    Args:
        lista (list): Lista de diccionarios que representan películas.
        genero (str): Género por el cual se quiere filtrar.

    Returns:
        list: Lista de diccionarios que representan películas del género seleccionado.
    """
    lista_filtrada = []
    for el in lista:
        if el["genero"] == genero:
            lista_filtrada.append(el)
    return lista_filtrada


def escribir_csv(lista: list, nombre_archivo):
    """Escribe una lista de películas en un archivo CSV.

    Args:
        lista (list): Lista de diccionarios que representan películas.
        nombre_archivo (str): Nombre del archivo CSV de salida.
    """
    if not lista:
        print(f"No hay películas del género '{nombre_archivo.split('.')[0]}' para escribir.")
        return

    with open(get_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for pelicula in lista:
            values = list(pelicula.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)
    print(f"Archivo '{nombre_archivo}' creado con éxito.")
   
   
def swap_lista(lista: list, i: int, j: int)->None:
    aux =  lista[i]
    lista[i] =lista[j]
    lista[j] =aux
     
def ordenar_peliculas_genero_rating(peliculas: dict)-> dict:
    """Ordena las películas por género y luego por rating .

    Args:
        peliculas (list): Lista de diccionarios que representan películas.

    Returns:
        list: Lista ordenada de películas.
    """
    TAM = len(peliculas)
    for i in range(TAM - 1):
        for j in range(i + 1, TAM):
            if peliculas[i]["genero"] == peliculas[j]["genero"]:
                if peliculas[i]["rating"] < peliculas[j]["rating"]:
                    swap_lista(peliculas, i, j)
            elif peliculas[i]["genero"] > peliculas[j]["genero"]:
                swap_lista(peliculas, i, j)
    return peliculas

def pelicula_mejor_rating(peliculas: list)-> tuple:
    """Muestra el título y el rating de la película con el rating más alto.

    Args:
        peliculas (list): Lista de diccionarios que representan películas.

    Returns:
        tuple: Tupla que contiene el título y el rating de la película con el mejor rating.
    """
    mejor_rating = None 
    mejor_pelicula = None 
    
    for pelicula in peliculas:
        if mejor_pelicula is None or pelicula["rating"] > mejor_rating:
            mejor_rating = pelicula["rating"]
            mejor_pelicula = pelicula
    
    return mejor_pelicula["titulo"], mejor_pelicula["rating"]

def guardar_peliculas_en_json(lista_peliculas: list)-> None:
    """Guarda el listado de películas en un archivo JSON.

    Args:
        lista_peliculas (list): Lista de diccionarios que representan películas.
        nombre_archivo (str): Nombre del archivo JSON de salida.
    """
    with open("peliculas.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_peliculas, archivo, indent=4)

    