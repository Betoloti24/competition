## IMPORTACION DE PAQUETES
from data.archive import inputDataBase
from controlers.textintable import printParticipants, printParticipantsByGroup, printParticipantsBySex, printTotalParticipants, printWinnersByGroup, printWinnersBySex, printWinnersByGroupSex, printWinner, printHistogram, printAverageTime
from collections import deque
import os, time

## DECLARACION DE FUNCIONES
# Funcion para la barra de carga
def progress(percent:int=0, width:int=30):
    left = width * percent // 100
    right = width - left
    print('\r\t[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

# Vista de la opcion 1 del menu principal
def menuArchivo(listparticipants:deque, listjuniors:deque, listseniors:deque, listmaster:deque, listmen:deque, listwomen:deque):
    # Inicializamos las variables y estructuras de datos
    option = -1
    namearchive = ""

    # Mostramos el menu de la opcion 1
    while (option):
        try:
            os.system('cls')
            print("\n\t**********************************")
            print(  "\t*        MENU DE ARCHIVOS        *")
            print(  "\t**********************************")
            print(  "\t* 1. CARGAR ARCHIVO              *")
            print(  "\t* 0. VOLVER AL MENU PRINCIPAL    *")
            print(  "\t**********************************")
            print(  "\t  Ingrese una opcion -->> ", end="") 
            option = int(input())

            # Evaluamos la opcion ingresada
            ## Opcion 1: Cargar archivo
            if (option == 1):
                os.system('cls')
                print("\n\tCARGAR ARCHIVO:\n")
                print("\tPara regresar al menu de archivos, ingrese el valor 0 y pulce ENTER")
                print("\tIngrese el nombre del archivo a cargar (nombre.txt) -->> ", end="")
                namearchive = input()

                if (namearchive != "0"):
                    # Pausa para la carga de datos
                    print("\n\tCARGANDO ARCHIVO...  \n\t", end="")
                    # for i in range(101):
                    #     progress(i)
                    #     time.sleep(0.05)
                    # print("")
                    
                    # Cargamos los datos del archivo
                    listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen = inputDataBase(namearchive, listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen)

            ## Opcion de salida
            elif (option == 0):
                return listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen

            ## Opcion incorrecta
            else:
                print("\n\t¡¡ERROR!!, ingrese una opcion correcta\n\n\t", end="")
                os.system("pause")

        ## Capturamos la excepcion de ValueError
        except ValueError:
            print("\n\t¡¡ERROR!!, el dato ingresado en el menú debe ser un número entero\n\n\t", end="")
            option = -1
            os.system("pause")

# Vista de la opcion 2 del menu principal
def menuAcciones(listparticipants:deque, listjuniors:deque, listseniors:deque, listmaster:deque, listmen:deque, listwomen:deque):
    # Inicializamos las variables y estructuras de datos
    option = -1

    # Mostramos el menu de la opcion 1
    while (option):
        try:
            os.system('cls')
            print("\n\t**************************************************")
            print(  "\t*                MENU DE ACCIONES                *")
            print(  "\t**************************************************")
            print(  "\t* 1. LISTA CON LA TOTALIDAD DE PARTICIPANTES     *")
            print(  "\t* 2. CANTIDAD TOTAL DE PARTICIPANTES             *")
            print(  "\t* 3. CANTIDAD DE PARTICIPANTES POR GRUPO ETARIO  *")
            print(  "\t* 4. CANTIDAD DE PARTICIPANTES POR SEXO          *")
            print(  "\t* 5. GANADORES POR GRUPO ETARIO                  *")
            print(  "\t* 6. GANADORES POR SEXO                          *")
            print(  "\t* 7. GANADORES POR GRUPO ETARIO Y SEXO           *")
            print(  "\t* 8. GANADOR GENERAL                             *")
            print(  "\t* 9. HISTOGRAMA DE PARTICIPANTE POR GRUPO ETARIO *")
            print(  "\t* 10. PROMEDIO DE TIEMPO POR GRUPO ETARIO Y SEXO *")
            print(  "\t* 0. VOLVER AL MENÚ PRINCIPAL                    *")
            print(  "\t**************************************************")
            print(  "\t  Ingrese una opcion -->> ", end="") 
            option = int(input())

            # Verificamos que la lista no este vacia
            if (len(listparticipants) != 0 and option != 0):
                # Evaluamos la opcion ingresada
                ## Opcion 1: Lista con la totalidad de participantes
                if (option == 1): printParticipants(listparticipants)
                ## Opcion 2: Cantidad total de participantes
                elif (option == 2): printTotalParticipants(listparticipants)
                ## Opcion 3: Cantidad de participantes por grupo etario
                elif (option == 3): printParticipantsByGroup(listjuniors, listmaster, listseniors)
                ## Opcion 4: Cantidad de participantes por sexo
                elif (option == 4): printParticipantsBySex(listmen, listwomen)
                ## Opcion 5: Ganadores por grupo etario
                elif (option == 5): printWinnersByGroup(listjuniors, listmaster, listseniors)
                ## Opcion 6: Ganadores por sexo
                elif (option == 6): printWinnersBySex(listmen, listwomen)
                ## Opcion 7: Ganadores por grupo etario y sexo
                elif (option == 7):
                    os.system('cls')
                    print("\n\tGANADORES POR SEXO Y ETARIO:\n")
                    printWinnersByGroupSex(listjuniors, listmaster, listseniors, listmen, listwomen)
                ## Opcion 8: Ganador general
                elif (option == 8): printWinner(listparticipants[0])
                ## Opcion 9: Histograma de participantes por grupo etario
                elif (option == 9): printHistogram(listjuniors, listseniors, listmaster)
                ## Opcion 10: Promedio de tiempo por grupo etario y sexo
                elif (option == 10): printAverageTime(listjuniors, listseniors, listmaster, listmen, listwomen)
                ## Opcion incorrecta
                elif (option != 0):
                    print("\n\tERROR!, ingrese una opcion correcta\n\n\t", end="")
            elif (option != 0):
                print("\n\t¡¡ERROR!!, la lista de participantes está vacía\n\n\t", end="")
                os.system("pause")
            os.system("pause")

        ## Capturamos la excepcion de ValueError
        except ValueError:
            print("\n\t¡¡ERROR!!, el dato ingresado en el menú debe ser un número entero\n\n\t", end="")
            option = -1
            os.system("pause")
        