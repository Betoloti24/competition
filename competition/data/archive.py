## Este modulo contiene todos los metodos que permiten la carga y validacion del archivo de texto con los datos a utilizar en el programa

## IMPORTACION DE PAQUETES
from exceptions.exepdatabase import FileNotExtension, FileEmpty, FileRegisterIncorrect
from datetime import time
from collections import deque
import os, sys

## DECLARACION DE FUNCIONES Y PROCEDIMIENTOS
# Procedimiento de validacion
def __validar(file):
    # Verificamos la extencion
    extension = file.name.split("/")[-1].split(".")[1]
    if extension not in ["txt", "md"]:
        raise FileNotExtension("¡¡ERROR!!, el archivo no es .txt ni .md")

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
    # Extraemos el directorio actual    
    dir_path = "/".join(sys.argv[0].split("/")[0:-1]) + "/data/"
    try:
        # Empezamos a trabajar con el archivo
        with open(dir_path + namearchive, "rt") as file:
            # Validamos el archivo
            if (__validar(file)):
                # Creamos las estructuras de la base de datos
                ## Lista de participantes
                listparticipants = list([
                    {"CI": data[0], "Apellido1": data[1], "Apellido2": data[2], "Nombre": data[3], "InicialNombre": data[4], "Sexo": data[5], "Edad": int(data[6]), "Tiempo": time(hour=int(data[7]), minute=int(data[8]), second=int(data[9]))}
                    for data in [line.split(",") for line in file.readlines()]
                ])
                listparticipants.sort(key=lambda participant: participant["Tiempo"])
                listparticipants = deque(listparticipants)

                ## Lista de participantes junior
                listjuniors = list(filter(lambda participant: participant["Edad"] <= 25, listparticipants))
                listjuniors.sort(key=lambda participant: participant["Tiempo"])
                listjuniors = deque(listjuniors)
                ## Lista de participantes senior
                listseniors = list(filter(lambda participant: participant["Edad"] > 25 and participant["Edad"] <= 40, listparticipants))
                listseniors.sort(key=lambda participant: participant["Tiempo"])
                listseniors = deque(listseniors)
                ## Lista de participantes master
                listmaster = list(filter(lambda participant: participant["Edad"] > 40, listparticipants))
                listmaster.sort(key=lambda participant: participant["Tiempo"])
                listmaster = deque(listmaster)
                ## Lista de participantes masculinos
                listmen = list(filter(lambda participant: participant["Sexo"] == "M", listparticipants))
                listmen.sort(key=lambda participant: participant["Tiempo"])
                listmen = deque(listmen)
                ## Lista de participantes femeninos
                listwomen = list(filter(lambda participant: participant["Sexo"] == "F", listparticipants))
                listwomen.sort(key=lambda participant: participant["Tiempo"])
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