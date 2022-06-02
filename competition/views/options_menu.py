## IMPORTACION DE PAQUETES
from data.archive import inputDataBase
from exceptions.exeption_basic import OptionMenu
from controllers.actions import (
    printParticipants, 
    printParticipantsByGroup, 
    printParticipantsBySex, 
    printTotalParticipants, 
    printWinnersByGroup, 
    printWinnersBySex, 
    printWinnersByGroupSex, 
    printWinner, 
    printHistogram, 
    printAverageTime)
from controllers.utils import clear_screen
import os, time

## DECLARACION DE FUNCIONES
# Funcion para la barra de carga
def progress(percent:int=0, width:int=30) -> None:
    left = width * percent // 100
    right = width - left
    print('\r\t[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

# Vista de la opcion 1 del menu principal
def menuArchivo(data_base:dict) -> dict:
    # Inicializamos las variables y estructuras de datos
    option = -1
    namearchive = ""

    # Mostramos el menu de la opcion 1
    while (option):
        try:
            clear_screen()
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
                clear_screen()
                print("\n\tCARGAR ARCHIVO:\n")
                print("\tNOTA: el archivo a cargar debe estar en la raiz del proyecto, junto al archivo main.py\n")
                print("\tPara regresar al menu de archivos, ingrese el valor 0 y pulce ENTER")
                print("\tIngrese el nombre del archivo a cargar (nombre.txt/md) -->> ", end="")
                namearchive = input()

                if (namearchive != "0"):
                    # Pausa para la carga de datos
                    print("\n\tCARGANDO ARCHIVO...   \n\t", end="")
                    for i in range(101):
                        progress(i)
                        time.sleep(0.05)
                    print("")
                    
                    # Cargamos los datos del archivo
                    data_base = inputDataBase(namearchive, data_base)

            ## Opcion de salida
            elif (option == 0):
                return data_base

            ## Opcion incorrecta
            else:
                raise OptionMenu("¡¡ERROR!!, el dato ingresado no es una opcion del menú")

        ## Capturamos la excepcion de ValueError
        except ValueError:
            print("\n\t¡¡ERROR!!, el dato ingresado en el menú debe ser un número entero\n\n\t", end="")
            option = -1
            input("Pulse ENTER para continuar... ")
        ## Capturamos la excepcion de OptionMenu
        except (OptionMenu) as e:
            print(f"\n\t{e}\n\n\t", end="")
            option = -1
            input("Pulse ENTER para continuar... ")

# Vista de la opcion 2 del menu principal
def menuAcciones(data_base:dict) -> dict:
    # Inicializamos las variables y estructuras de datos
    option = -1

    # Mostramos el menu de la opcion 1
    while (option):
        try:
            clear_screen()
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
            if (len(data_base["list_participants"]) != 0 and option != 0):
                # Evaluamos la opcion ingresada
                ## Opcion 1: Lista con la totalidad de participantes
                if (option == 1): printParticipants(data_base["list_participants"])
                ## Opcion 2: Cantidad total de participantes
                elif (option == 2): printTotalParticipants(data_base["list_participants"])
                ## Opcion 3: Cantidad de participantes por grupo etario
                elif (option == 3): printParticipantsByGroup(data_base["list_juniors"], data_base["list_masters"], data_base["list_seniors"])
                ## Opcion 4: Cantidad de participantes por sexo
                elif (option == 4): printParticipantsBySex(data_base["list_men"], data_base["list_women"])
                ## Opcion 5: Ganadores por grupo etario
                elif (option == 5): printWinnersByGroup(data_base["list_juniors"], data_base["list_masters"], data_base["list_seniors"])
                ## Opcion 6: Ganadores por sexo
                elif (option == 6): printWinnersBySex(data_base["list_men"], data_base["list_women"])
                ## Opcion 7: Ganadores por grupo etario y sexo
                elif (option == 7):
                    clear_screen()
                    print("\n\tGANADORES POR SEXO Y ETARIO:\n")
                    printWinnersByGroupSex(data_base["list_juniors"], data_base["list_masters"], data_base["list_seniors"])
                ## Opcion 8: Ganador general
                elif (option == 8): printWinner(data_base["list_participants"][0])
                ## Opcion 9: Histograma de participantes por grupo etario
                elif (option == 9): printHistogram(data_base["list_juniors"], data_base["list_seniors"], data_base["list_masters"])
                ## Opcion 10: Promedio de tiempo por grupo etario y sexo
                elif (option == 10): printAverageTime(data_base["list_juniors"], data_base["list_seniors"], data_base["list_masters"])
                ## Opcion incorrecta
                elif (option != 0):
                    raise OptionMenu("¡¡ERROR!!, el dato ingresado no es una opcion del menú")
                input("Pulse ENTER para continuar... ")
            elif (len(data_base["list_participants"]) == 0 and option != 0):
                raise OptionMenu("¡¡ERROR!!, la lista de participantes está vacía, carge un archivo con los datos")
            
        ## Capturamos la excepcion de ValueError
        except ValueError:
            print("\n\t¡¡ERROR!!, el dato ingresado en el menú debe ser un número entero\n\n\t", end="")
            option = -1
            input("Pulse ENTER para continuar... ")

        ## Capturamos la excepcion de OptionMenu
        except (OptionMenu) as e:
            print(f"\n\t{e}\n\n\t", end="")
            option = -1
            input("Pulse ENTER para continuar... ")
        