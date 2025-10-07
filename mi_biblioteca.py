
lista_estudiantes = ["Dario Villanustre", "Belen Gomez", "Kymbo Sanchez"]
lista_genero = ["M", "F", "X"]
lista_legajos = [125620, 154289, 125945]
lista_estados = [1, 0, 1]
lista_notas = [[9,8,10,9,9], 
               [9,6,7,6,5], 
               [9,6,7,8,8]]

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)-> list:
    matriz = []
    for indice in range(cantidad_filas): #recorre cada fila de la matriz 
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila] # Agrego la fila cargada a la matriz 
    return matriz

def cargar_notas_en_matriz(matriz:list):
    for indice in range (len(matriz)): #recorre las filas 
        for j in range(len(matriz[indice])): #recorre las columnas dentro de la fila indice
            matriz[indice][j] = lista_notas [indice][j] #Asigna a cada celda de la matriz el valor correspondiente de lista_notas
    return matriz

def mostrar_matriz(matriz:list): 
    for indice in range(len(matriz)):
        for j in range(len(matriz[indice])):
                print(matriz[indice][j], end = " ") 
        print(" ")

def calcular_promedios(matriz:list):
    lista_notas = []
    for indice in range(len(matriz)):
        acumulador = 0
        for j in range(len(matriz[indice])):
            acumulador += matriz[indice][j]
        lista_promedio = acumulador / len(matriz[indice])
        lista_notas += [lista_promedio]

    for i in range(len(lista_notas)):
        if i == len(lista_notas) - 1:
            print(lista_notas[i])
        else:
            print(lista_notas[i], end= " - ")
    return lista_notas

def mostrar_un_estudiante(estudiantes:list, generos:list, legajos:list, estados:list, notas:list, indice:int): #llamarla dentro de la 2da
    print("Nombre del estudiante:", estudiantes[indice])
    print("Genero:", generos[indice])
    print("Numero de legajo:",legajos[indice])
    print("Estado:", estados[indice])
    print("Notas:",notas[indice])
    print ("-" * 30)
        
def mostrar_estudiantes_activos(estudiantes:list, generos:list, legajos:list, estados:list, notas:list ):
         for indice in range(len(estudiantes)):
            if estados[indice] == 1:
                mostrar_un_estudiante(estudiantes, generos, legajos, estados, notas, indice)


def mostrar_promedios_ordenados(lista_notas:list, criterio:str = "asc"):
    n = len(lista_notas)
    for indice in range(n):
          for j in range(0, n -indice -1):
            if (criterio == "asc" and lista_notas [j] > lista_notas[j + 1]) or (criterio == "desc" and lista_notas[j] < lista_notas[j + 1]):
                    aux = lista_notas[j]
                    lista_notas[j] = lista_notas[j+1]
                    lista_notas[j+1] = aux  

    for i in range(len(lista_notas)):
        if i == len(lista_notas) - 1:
            print(lista_notas[i])
        else:
            print(lista_notas[i], end= " - ")
    return lista_notas      


def identificar_materia_mayor_promedio(matriz_cargada:list):
    lista_notas_acumuladas = [0] * 5
    lista_notas = [0] * 5

    for i in range(len(matriz_cargada)):
        for j in range(len(matriz_cargada[i])):
             lista_notas_acumuladas[j] += matriz_cargada[i][j]
    
    for i in range(len(lista_notas_acumuladas)):
         lista_promedio = lista_notas_acumuladas[i] / len(matriz_cargada)
         lista_notas[i] = lista_promedio
    
    for i in range(len(lista_notas)):
        mostrar_una_materia(i, lista_notas[i])

    promedio_mayor = lista_notas[0]
    for i in range(1, len(lista_notas)):
        if lista_notas[i] > promedio_mayor:
            promedio_mayor = lista_notas[i]
    return promedio_mayor
        
def mostrar_una_materia(i, lista_notas):
     print("Materia_", i+1, lista_notas)

def buscar_por_legajo(legajos:list, legajo_buscado:int):
     for indice in range(len(legajos)):
          if legajos[indice] == legajo_buscado:
               return indice
          
def devolver_estudiante(indice_encontrado:int):
    datos_de_un_estudiante = []
    for i in range (len(lista_estudiantes)):
         if i == indice_encontrado:
              datos_de_un_estudiante = [lista_estudiantes[i], lista_estados[i], lista_genero[i], lista_notas[i]]

    return datos_de_un_estudiante

def mostrar_estudiante_encontrado(datos:list):

    print("Nombre:",datos[0])
    print("estado:",datos[1])
    print("Genero:",datos[2])
    print("Notas:",datos[3])

def mostrar_repeticion_de_notas(matriz_cargada:list, indice_materia:int):
    lista_notas = [0] * 10
    for i in range(len(matriz_cargada)):
        nota = matriz_cargada[i][indice_materia-1]
        lista_notas[nota-1] += 1
    for i in range(len(lista_notas)):
        if i == len(lista_notas) - 1:
            print(lista_notas[i])
        else:
            print(lista_notas[i], end= " - ")
    return lista_notas

   


