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
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["ci"], participant["name"], participant["initialname"], participant["surname1"], participant["surname2"], participant["sex"], participant["age"], participant["time"].strftime("%H:%M:%S")))
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
    
    ## Imprimimos a los ganadores por grupo etario
    print("\t----------------------------------------------------------------------------------------------------")
    print("\t|  Grupo  |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------------")
   
    ## Imprimimos los datos del ganador junior
    print("\t| Junior  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(listjunior[0]["ci"], listjunior[0]["name"], listjunior[0]["initialname"], listjunior[0]["surname1"], listjunior[0]["surname2"], listjunior[0]["sex"], listjunior[0]["age"], listjunior[0]["time"].strftime("%H:%M:%S")))
    ## Imprimimos los datos del ganador senior
    print("\t| Senior  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(listsenior[0]["ci"], listsenior[0]["name"], listsenior[0]["initialname"], listsenior[0]["surname1"], listsenior[0]["surname2"], listsenior[0]["sex"], listsenior[0]["age"], listsenior[0]["time"].strftime("%H:%M:%S")))
    ## Imprimimos los datos del ganador master
    print("\t| Master  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(listmaster[0]["ci"], listmaster[0]["name"], listmaster[0]["initialname"], listmaster[0]["surname1"], listmaster[0]["surname2"], listmaster[0]["sex"], listmaster[0]["age"], listmaster[0]["time"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion para imprimir los ganadores por sexo
def printWinnersBySex(listmen:deque, listwomen:deque):
    # Impresion de resultados formateados en tabla
    os.system('cls')
    ## Imprimimos el encabezado
    print("\n\tGANADORES POR SEXO:\n")
    ## Imprimimos a los ganadores por sexo
    print("\t------------------------------------------------------------------------------------------------------")
    print("\t|   Grupo   |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t------------------------------------------------------------------------------------------------------")
    print("\t| Femenino  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(listwomen[0]["ci"], listwomen[0]["name"], listwomen[0]["initialname"], listwomen[0]["surname1"], listwomen[0]["surname2"], listwomen[0]["sex"], listwomen[0]["age"], listwomen[0]["time"].strftime("%H:%M:%S")))
    print("\t| Masculino | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(listmen[0]["ci"], listmen[0]["name"], listmen[0]["initialname"], listmen[0]["surname1"], listmen[0]["surname2"], listmen[0]["sex"], listmen[0]["age"], listmen[0]["time"].strftime("%H:%M:%S")))
    print("\t------------------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion para imprimir los ganadores por etario y sexo
def printWinnersByGroupSex(listmen:deque, listwomen:deque, listjunior:deque, listsenior:deque, listmaster:deque):
    # Impresion de resultados formateados en tabla
    ## Imprimimos por sexo
    printWinnersBySex(listmen, listwomen)
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
    print("\t  Cedula de Identidad: {}, Nombre: {}, Inicial del 2do Nombre: {}, 1er Apellido: {}, 2do Apellido: {}, Sexo: {}, Edad: {} años de edad, Tiempo Record: {}\n\n\t".format(winner["ci"], winner["name"], winner["initialname"], winner["surname1"], winner["surname2"], winner["sex"], winner["age"], winner["time"].strftime("%H:%M:%S")), end="")

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
    fseconds = lambda ptime: ptime['time'].hour*3600 + ptime['time'].minute*60 + ptime['time'].second
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