from menu import *
from funciones import *

while True:
    
    match menu():
        case 1:
            lista_peliculas = cargar_csv()
        case 2:
            imprimir_lista(lista_peliculas)
        case 3:
            lista_peliculas_con_rating = mapear_peliculas(rating_random, lista_peliculas)
            imprimir_lista(lista_peliculas_con_rating)
        case 4:
            lista_peliculas_con_genero = mapear_peliculas(asignar_genero, lista_peliculas)
            imprimir_lista(lista_peliculas_con_genero)
        case 5:
            genero_seleccionado = input("Ingrese el género por el cual filtrar (drama, comedia, acción, terror): ").lower()
            peliculas_filtradas = filtrar_peliculas_genero(lista_peliculas_con_genero, genero_seleccionado)
            nombre_archivo_salida = f"{genero_seleccionado}s.csv"
            escribir_csv(peliculas_filtradas, nombre_archivo_salida)
        case 6:
            lista_peliculas_ordenadas = ordenar_peliculas_genero_rating(lista_peliculas)
            imprimir_lista(lista_peliculas_ordenadas)
        case 7:
            mejor_titulo, mejor_rating = pelicula_mejor_rating(lista_peliculas)
            print(f"La mejor pelicula es '{mejor_titulo}' con un rating de {mejor_rating}.")
        case 8:
            guardar_peliculas_en_json(lista_peliculas)
        case 9:
            break
        case _:
            print("Opcion no valida")
        
    pausar()