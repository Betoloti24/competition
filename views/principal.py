## IMPORTACION DE PAQUETES
from .options_menu import menuArchivo, menuAcciones
from controllers.utils import clear_screen
from exceptions.exeption_basic import OptionMenu
import os

## DECLARACION DE FUNCIONES Y PROCEDIMIENTOS
# Vista principal del sistema 
def menuPrincipal() -> None:
    # Inicializamos las variables y estructuras de datos
    option = -1
    data_base = {"list_participants": [], "list_juniors": [], "list_seniors": [], "list_master": [], "list_men": [], "list_women": []}

    # Mostramos el menu principal
    while (option):
        try:
            clear_screen()
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
                data_base = menuArchivo(data_base)
            ## Opcion 2: Menu de acciones
            elif (option == 2):
                menuAcciones(data_base)
            ## Opcion 0: Salir del sistema
            elif (option == 0):
                print("\n\tGracias por usar este sistema\n\n\t", end="")
                input("Pulse ENTER para continuar... ")
                clear_screen()
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
