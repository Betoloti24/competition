## Este modulo posee todos los metodos que conforman la impresion de datos en formato de tabla

## IMPORTACION DE PAQUETES
from collections import deque
from statistics import mean
from datetime import timedelta
import os

## DEFINICION DE FUNCIONES
# Funcion para imprimir la tabla con los datos de todos los participantes
def printParticipants(listparticipants:deque):
    # Impresion de resultados formateados en tabla
    ## Imprimimos el encabezado
    print("\n\t DATOS DE LOS PARTICIPANTES:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(listparticipants):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["CI"], participant["Nombre"], participant["InicialNombre"], participant["Apellido1"], participant["Apellido2"], participant["Sexo"], participant["Edad"], participant["Tiempo"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion que imprime la cantidad de participantes
def printTotalParticipants(listparticipants:deque):
    # Impresion de resultados formateados en la linea
    os.system('cls')
    print(f"\n\tCANTIDAD DE PARTICIPANTES:\n\n\tSe poseen un total de {len(listparticipants)} participantes registrados\n\n\t", end="")

# Funcion que imprime una tabla con la cantidad de participantes por grupo etario
def printParticipantsByGroup(listjunior:deque, listmaster:deque, listsenior:deque):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tDATOS DE LOS PARTICIPANTES POR GRUPO ETARIO:\n")
    print("\t------------------------")
    print("\t|#|  Grupo  | Cantidad |")
    print("\t------------------------")
    ## Imprimimos los datos de cada participante
    print("\t|{:1}| {:8}|{:7}   |".format(1, "Junior", len(listjunior)))
    print("\t|{:1}| {:8}|{:7}   |".format(2, "Senior", len(listsenior)))
    print("\t|{:1}| {:8}|{:7}   |".format(3, "Master", len(listmaster)))
    print("\t------------------------")
    print("\t|   Total:       {:3}   |".format(len(listjunior)+len(listsenior)+len(listmaster)))
    print("\t------------------------\n\n\t", end="")

# Funcion que imprime una tabla con la cantidad de participantes por sexo
def printParticipantsBySex(listmen:deque, listwomen:deque):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tDATOS DE LOS PARTICIPANTES POR SEXO:\n")
    print("\t-------------------------")
    print("\t|#|   Sexo   | Cantidad |")
    print("\t-------------------------")
    ## Imprimimos los datos de cada participante
    print("\t|{:1}| {:9}|{:7}   |".format(1, "Hombres", len(listmen)))
    print("\t|{:1}| {:9}|{:7}   |".format(2, "Mujeres", len(listwomen)))
    print("\t-------------------------")
    print("\t|   Total:        {:3}   |".format(len(listmen)+len(listwomen)))
    print("\t-------------------------\n\n\t", end="")

# Funcion que imprime los gananadores por grupo etario
def printWinnersByGroup(listjunior:deque, listsenior:deque, listmaster:deque):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    
    ## Imprimimos el encabezado
    print("\n\tGANADORES POR GRUPO ETARIO:\n")
    
    ## Imprimimos a los juniors
    print("\tGRUPO DE JUNIORS:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(listjunior):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["CI"], participant["Nombre"], participant["InicialNombre"], participant["Apellido1"], participant["Apellido2"], participant["Sexo"], participant["Edad"], participant["Tiempo"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n", end="")

    ## Imprimimos a los seniors
    print("\tGRUPO DE SENIORS:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(listsenior):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["CI"], participant["Nombre"], participant["InicialNombre"], participant["Apellido1"], participant["Apellido2"], participant["Sexo"], participant["Edad"], participant["Tiempo"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n", end="")
    
    ## Imprimimos a los masters
    print("\tGRUPO DE MASTERS:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(listmaster):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["CI"], participant["Nombre"], participant["InicialNombre"], participant["Apellido1"], participant["Apellido2"], participant["Sexo"], participant["Edad"], participant["Tiempo"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion para imprimir los ganadores por sexo
def printWinnersBySex(listmen:deque, listwomen:deque):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tGANADORES POR SEXO:\n")
    ## Imprimimos a las Mujeres
    print("\tGRUPO DE MUJERES:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(listwomen):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["CI"], participant["Nombre"], participant["InicialNombre"], participant["Apellido1"], participant["Apellido2"], participant["Sexo"], participant["Edad"], participant["Tiempo"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n", end="")
    
    ## Imprimimos a los Hombres
    print("\tGRUPO DE HOMBRES:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(listmen):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["CI"], participant["Nombre"], participant["InicialNombre"], participant["Apellido1"], participant["Apellido2"], participant["Sexo"], participant["Edad"], participant["Tiempo"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion para imprimir los ganadores por etario y sexo
def printWinnersByGroupSex(listmen:deque, listwomen:deque, listjunior:deque, listsenior:deque, listmaster:deque):
    # Impresion de resultados formateados en tabla
    ## Imprimimos por sexo
    printWinnersBySex(listmen, listwomen)
    os.system('pause')
    ## Imprimimos por etario
    printWinnersByGroup(listjunior, listsenior, listmaster)

# Funcion para imprimir al ganador general
def printWinner(winner:dict):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tGANADOR GENERAL:\n")
    ## Imprimimos los datos del ganador
    print("\tEntre todos los participantes, el que posee el mejor tiempo es:\n")
    print("\t\tCedula de Identidad: {:9}\n\t\tNombre: {:13}\n\t\tInicial del 2do Nombre: {:4}\n\t\t1er Apellido: {:13}\n\t\t2do Apellido: {:17}\n\t\tSexo: {:3}\n\t\tEdad: {:3} años de edad\n\t\tTiempo Record: {:9}\n\n\t".format(winner["CI"], winner["Nombre"], winner["InicialNombre"], winner["Apellido1"], winner["Apellido2"], winner["Sexo"], winner["Edad"], winner["Tiempo"].strftime("%H:%M:%S")), end="")

# Funcion para imprimir el histograma de participantes por grupo etario
def printHistogram(listjunior:deque, listsenior:deque, listmaster:deque):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tHISTOGRAMA DE PARTICIPANTES POR GRUPO ETARIO:\n")
    ## Imprimimos los datos de cada participante
    print("\tJunior(x): ", "| ", "*" * len(listjunior))
    print("\tSenior(y): ", "| ", "*" * len(listsenior))
    print("\tMaster(z): ", "| ", "*" * len(listmaster), "\n\n\t", end="")

# Funcion para mostrar el promedio de tiempo de los grupos etarios y el sexo
def printAverageTime(listjunior:deque, listsenior:deque, listmaster:deque, listmen:deque, listwomen:deque):
    # Declaracion de variables
    fseconds = lambda ptime: ptime['Tiempo'].hour*3600 + ptime['Tiempo'].minute*60 + ptime['Tiempo'].second
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tPROMEDIO DE TIEMPO POR GRUPO ETARIO Y SEXO:\n")
    ## Imprimimos los datos de cada participante
    print(f"\tEl promedio en tiempo de los participantes Junior es de: {str(timedelta(seconds=int(mean(list(map(fseconds, listjunior))))))} horas")
    print(f"\tEl promedio en tiempo de los participantes Senior es de: {str(timedelta(seconds=int(mean(list(map(fseconds, listsenior))))))} horas")
    print(f"\tEl promedio en tiempo de los participantes Master es de: {str(timedelta(seconds=int(mean(list(map(fseconds, listmaster))))))} horas")
    print(f"\tEl promedio en tiempo de los participantes Mujeres es de: {str(timedelta(seconds=int(mean(list(map(fseconds, listwomen))))))} horas")
    print(f"\tEl promedio en tiempo de los participantes Hombres es de: {str(timedelta(seconds=int(mean(list(map(fseconds, listmen))))))} horas")
    print("\n\t", end="")