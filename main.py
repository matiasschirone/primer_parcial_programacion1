from menu import *
from funciones import *

csv_cargado = False
genero_asignado = False
rating_asignado = False

while True:
    
    match menu():
        case 1:
            csv_cargado = True
            lista_peliculas = cargar_csv()
        case 2:
            if csv_cargado:
                imprimir_lista(lista_peliculas)
            else:
                print("Debes cargar el CSV primero.")
        case 3:
            if csv_cargado:
                lista_peliculas_con_rating = mapear_peliculas(rating_random, lista_peliculas)
                imprimir_lista(lista_peliculas_con_rating)
                rating_asignado = True
            else:
                print("Debes cargar el CSV primero.")
        case 4:
            if csv_cargado:
                lista_peliculas_con_genero = mapear_peliculas(asignar_genero, lista_peliculas)
                imprimir_lista(lista_peliculas_con_genero)
                genero_asignado = True
            else:
                print("Debes cargar el CSV primero.")
        case 5:
            if csv_cargado:
                if genero_asignado:
                    genero_seleccionado = input("Ingrese el género por el cual filtrar (drama, comedia, acción, terror): ").lower()
                    peliculas_filtradas = filtrar_peliculas_genero(lista_peliculas_con_genero, genero_seleccionado)
                    nombre_archivo_salida = f"{genero_seleccionado}s.csv"
                    escribir_csv(peliculas_filtradas, nombre_archivo_salida)
                else:
                    print("Debes asignar un género primero.")
            else:
                print("Debes cargar el CSV primero.")
        case 6:
            if csv_cargado and genero_asignado:
                if rating_asignado:
                    lista_peliculas_ordenadas = ordenar_peliculas_genero_rating(lista_peliculas)
                    imprimir_lista(lista_peliculas_ordenadas)
                else:
                    print("Debes asignar un rating primero.")
            else:
                print("Debes cargar el CSV y asignar un género primero.")
        case 7:
            if csv_cargado and rating_asignado:
                mejor_titulo, mejor_rating = pelicula_mejor_rating(lista_peliculas)
                print(f"La mejor pelicula es '{mejor_titulo}' con un rating de {mejor_rating}.")
            else:
                print("Debes cargar el CSV primero.")
        case 8:
            if csv_cargado:
                guardar_peliculas_en_json(lista_peliculas)
            else:
                print("Debes cargar el CSV primero.")
        case 9:
            break
        case _:
            print("Opcion no valida")
        
    pausar()