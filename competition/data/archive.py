## Este modulo contiene todos los metodos que permiten la carga y validacion del archivo de texto con los datos a utilizar en el programa

## IMPORTACION DE PAQUETES
from exceptions.exepdatabase import FileNotExtension, FileEmpty, FileRegisterIncorrect
from datetime import time
from collections import deque
import os, sys

## DECLARACION DE FUNCIONES Y PROCEDIMIENTOS
# Procedimiento de validacion
def __validar(file):
    # Verificamos que el archivo no este vacio
    if (file.read() == ""):
        raise FileEmpty("¡¡ERROR!!, el archivo esta vacio")
    # Volvemos a colocar el apuntador al inicio del archivo
    file.seek(0,0)

    # Verificamos que el archivo posea los registros correctos
    if (len(list(filter(lambda line: line.count(",") != 9, file.readlines()))) != 0):
        file.seek(0,0)
        raise FileRegisterIncorrect("¡¡ERROR!!, el archivo no posee la cantidad de campos por registros correctos")
    # Volvemos a colocar el apuntador al inicio del archivo
    file.seek(0,0)
    return True

# Carga del archivo
def inputDataBase(namearchive:str, listparticipants:deque, listjuniors:deque, listseniors:deque, listmaster:deque, listmen:deque, listwomen:deque):
    try:
        # Empezamos a trabajar con el archivo
        with open(namearchive + ".txt", "rt") as file:
            # Validamos el archivo
            if (__validar(file)):
                # Creamos las estructuras de la base de datos
                ## Lista de participantes
                listparticipants = list([
                    {"ci": data[0], "surname1": data[1], "surname2": data[2], "name": data[3], "initialname": data[4], "sex": data[5], "age": int(data[6]), "time": time(hour=int(data[7]), minute=int(data[8]), second=int(data[9]))}
                    for data in [line.split(",") for line in file.readlines()]
                ])
                listparticipants.sort(key=lambda participant: participant["time"])
                listparticipants = deque(listparticipants)

                ## Lista de participantes junior
                listjuniors = list(filter(lambda participant: participant["age"] <= 25, listparticipants))
                listjuniors.sort(key=lambda participant: participant["time"])
                listjuniors = deque(listjuniors)
                ## Lista de participantes senior
                listseniors = list(filter(lambda participant: participant["age"] > 25 and participant["age"] <= 40, listparticipants))
                listseniors.sort(key=lambda participant: participant["time"])
                listseniors = deque(listseniors)
                ## Lista de participantes master
                listmaster = list(filter(lambda participant: participant["age"] > 40, listparticipants))
                listmaster.sort(key=lambda participant: participant["time"])
                listmaster = deque(listmaster)
                ## Lista de participantes masculinos
                listmen = list(filter(lambda participant: participant["sex"] == "M", listparticipants))
                listmen.sort(key=lambda participant: participant["time"])
                listmen = deque(listmen)
                ## Lista de participantes femeninos
                listwomen = list(filter(lambda participant: participant["sex"] == "F", listparticipants))
                listwomen.sort(key=lambda participant: participant["time"])
                listwomen = deque(listwomen)

    # Capturamos la excepcion de FileNotFoundError
    except FileNotFoundError:
        print("\n\tERROR!, el archivo no existe\n\n\t", end="")
        os.system("pause")
    # Capturamos la excepcion de FileNotExtension
    except (FileNotExtension, FileEmpty, FileRegisterIncorrect) as e:
        print(f"\n\t{e}\n\n\t", end="")
        os.system("pause")
    # Capturamos el exito de la carga
    else:
        print("\n\t¡¡DATOS CARGADOS CON EXITO DEL ARCHIVO!!\n\n\t", end="")
        os.system("pause")
    # Retornamos por finalizacion
    finally:
        return listparticipants, listjuniors, listseniors, listmaster, listmen, listwomen

# Bloque para las pruebas del script
if __name__ == "__main__":
    inputDataBase([])