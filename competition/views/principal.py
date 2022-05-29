## IMPORTACION DE PAQUETES
from .optionsmenu import menuArchivo, menuAcciones
from collections import deque
import os

## DECLARACION DE FUNCIONES Y PROCEDIMIENTOS
# Vista principal del sistema
def menuPrincipal():
    # Inicializamos las variables y estructuras de datos
    option = -1
    listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen = deque([]), deque([]), deque([]), deque([]), deque([]), deque([]),

    # Mostramos el menu principal
    while (option):
        try:
            os.system('cls')
            print("\n\t**********************************")
            print(  "\t*   MENU PRINCIPAL DEL SISTEMA   *")
            print(  "\t**********************************")
            print(  "\t* 1. ARCHIVOS                    *")
            print(  "\t* 2. ACCIONES                    *")
            print(  "\t* 0. SALIR                       *")
            print(  "\t**********************************")
            print(  "\t  Ingrese una opcion -->> ", end="") 
            option = int(input())

            # Evaluamos la opcion ingresada
            ## Opcion 1: Menu de archivos
            if (option == 1):
                listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen = menuArchivo(listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen)
            ## Opcion 2: Menu de acciones
            elif (option == 2):
                menuAcciones(listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen)
            ## Opcion 0: Salir del sistema
            elif (option == 0):
                print("\n\tGracias por usar este sistema\n\n\t", end="")
                os.system("pause")
                os.system('cls')
            ## Opcion incorrecta
            else:
                print("\n\t¡¡ERROR!!, ingrese una opcion correcta\n\n\t", end="")
                os.system("pause")

        ## Capturamos la excepcion de ValueError
        except ValueError:
            print("\n\t¡¡ERROR!!, el dato ingresado en el menú debe ser un número entero\n\n\t", end="")
            option = -1
            os.system("pause")
