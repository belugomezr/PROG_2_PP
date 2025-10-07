
#lista_estudiantes = [""] * 3
#lista_genero = [""] * 3
#lista_legajos = [0] * 3
#lista_notas = [0] * 5



def validar_genero(lista:list, i:int):
    genero = input("Ingrese el genero M, F, X: ")
    while genero != "M" and genero != "F" and genero != "X":
        genero = input("Dato incorrecto. Ingrese nuevamente el genero: ")
    lista[i] = genero 

def validar_legajos(lista:list, i:int):
    legajos = int(input("Ingrese el numero de legajo: "))
    while legajos < 100000 or legajos > 999999:
        legajos = int(input("Error. Ingrese un legajo de 6 digitos: "))
    lista[i] = legajos

def validar_estados(lista:list, i:int):
    estados = int(input("Ingresar el estado del estudiante: "))
    while estados != 1 and estados != 2:
        estados = int(input("Error. Ingrese un numero valido 1 o 2: "))
    lista[i] = estados

def validar_notas(lista:list, i:int):
    nota = int(input("Ingresa la nota el estudiante: "))
    while nota <= 0 or nota > 10:
        nota = int(input("Error. Ingrese un numero entre 1 y 10:"))
    lista[i] = nota

def cargar_datos(lista_estudiantes, lista_legajos, lista_genero, lista_notas):
    print("CARGA DE DATOS DE ESTUDIANTES\n")
    for i in range(3):  
        print(f"--- Estudiante {i+1} ---")
        lista_estudiantes[i] = input("Ingrese el nombre del estudiante: ")
        validar_legajos(lista_legajos, i)
        validar_genero(lista_genero, i)
        for i in range(5):
            validar_notas(lista_notas, i)
    print("Carga finalizada correctamente.\n")

#cargar_datos(lista_estudiantes, lista_legajos, lista_genero, lista_notas)



