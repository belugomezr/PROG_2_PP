
from mi_biblioteca import *
from validaciones import *


menu = """
==================================
MENÚ PRINCIPAL
1. Cargar datos de los estudiantes
2. Mostrar datos de estudiantes activos
3. Mostrar promedios de estudiantes
4. Mostrar promedios ordenados
5. Mostrar materia con mayor promedio
6. Buscar estudiante por legajo
7. Mostrar cantidad de repeticiones de notas
8. Salir
==================================
Opcion: """
    

def mostrar_menu(menu):
    matriz = []
    while True:
        opcion_seleccionada = input(menu)
        match opcion_seleccionada:
            case "1":
                cargar_datos(lista_estudiantes, lista_legajos, lista_genero, lista_notas)
                # matriz = inicializar_matriz(3,5,None)
                # cargar_notas_en_matriz(matriz)
                # print("Notas: ")
                # mostrar_matriz(matriz)
            case "2":
                mostrar_estudiantes_activos(lista_estudiantes, lista_genero, lista_legajos,lista_estados, lista_notas)
                mostrar_un_estudiante(lista_estudiantes, lista_genero, lista_legajos,lista_estados, lista_notas, 2)
            case "3":
                print("Promedios de los estudiantes:")
                lista_promedios = calcular_promedios(matriz)
            case "4":
                print("Promedios ordenados: ")
                lista_ordenada = mostrar_promedios_ordenados(lista_promedios, "desc")
            case "5":
                identificar_materia_mayor_promedio(matriz)
            case "6":
                indice_encontrado = buscar_por_legajo(lista_legajos, 125945 )
                datos_estudiantes = devolver_estudiante(indice_encontrado)
                mostrar_estudiante_encontrado(datos_estudiantes)
            case "7":
                mostrar_repeticion_de_notas(matriz, 2)
            case "8":
                print("Fin del programa")
                break
            case _:
                print("Opcion no valida. Ingrese una opcion nuevamente: ")

mostrar_menu(menu)
        
                




