## Este modulo contiene todos los metodos que permiten la carga y validacion del archivo de texto con los datos a utilizar en el programa

## IMPORTACION DE PAQUETES
from exceptions.exepdatabase import FileEmpty, FileRegisterIncorrect
from datetime import time
from collections import deque
import os, sys

## DECLARACION DE FUNCIONES Y PROCEDIMIENTOS
# Procedimiento de validacion
def __validar(file):
    # Validamos si es un archivo de texto, si arroja una excepcion de tipo ValueError, no es un archivo de texto
    file.read()
    file.seek(0,0)

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
def inputDataBase(name_archive:str, data_base:dict):
    try:
        # Empezamos a trabajar con el archivo
        with open(name_archive, "r") as file:
            # Validamos el archivo
            if (__validar(file)):
                # Creamos las estructuras de la base de datos
                ## Lista de participantes
                data_base["list_participants"] = list([
                    {"ci": data[0], "surname1": data[1], "surname2": data[2], "name": data[3], "initialname": data[4], "sex": data[5], "age": int(data[6]), "time": time(hour=int(data[7]), minute=int(data[8]), second=int(data[9]))}
                    for data in [line.split(",") for line in file.readlines()]
                ])
                data_base["list_participants"].sort(key=lambda participant: participant["time"])
                data_base["list_participants"] = deque(data_base["list_participants"])

                ## Lista de participantes junior
                data_base["list_juniors"] = list(filter(lambda participant: participant["age"] <= 25, data_base["list_participants"]))
                data_base["list_juniors"].sort(key=lambda participant: participant["time"])
                data_base["list_juniors"] = deque(data_base["list_juniors"])
                ## Lista de participantes senior
                data_base["list_seniors"] = list(filter(lambda participant: participant["age"] > 25 and participant["age"] <= 40, data_base["list_participants"]))
                data_base["list_seniors"].sort(key=lambda participant: participant["time"])
                data_base["list_seniors"] = deque(data_base["list_seniors"])
                ## Lista de participantes master
                data_base["list_masters"] = list(filter(lambda participant: participant["age"] > 40, data_base["list_participants"]))
                data_base["list_masters"].sort(key=lambda participant: participant["time"])
                data_base["list_masters"] = deque(data_base["list_masters"])
                ## Lista de participantes masculinos
                data_base["list_men"] = list(filter(lambda participant: participant["sex"] == "M", data_base["list_participants"]))
                data_base["list_men"].sort(key=lambda participant: participant["time"])
                data_base["list_men"] = deque(data_base["list_men"])
                ## Lista de participantes femeninos
                data_base["list_women"] = list(filter(lambda participant: participant["sex"] == "F", data_base["list_participants"]))
                data_base["list_women"].sort(key=lambda participant: participant["time"])
                data_base["list_women"] = deque(data_base["list_women"])

    # Capturamos la excepcion de FileNotFoundError
    except FileNotFoundError:
        print("\n\t¡ERROR!, el archivo no existe\n\n\t", end="")
        os.system("pause")
    # Capturamos la excepcion de FileNotExtension
    except (FileEmpty, FileRegisterIncorrect) as e:
        print(f"\n\t{e}\n\n\t", end="")
        os.system("pause")
    # Capturamos que se haya ingresado un archivo que no es de texto
    except ValueError:
        print("\n\t¡ERROR!, el archivo ingresado no es de texto\n\n\t", end="")
        os.system("pause")
    # Capturamos el exito de la carga
    else:
        print("\n\t¡¡DATOS CARGADOS CON EXITO DEL ARCHIVO!!\n\n", end="")
        route = sys.path[0].replace('\\\\', '\\')
        print(f"\tEl archivo cargado fue: {route}\\{ name_archive}\n\n\t", end="")
        os.system("pause")
    # Retornamos por finalizacion
    finally:
        return data_base

# Bloque para las pruebas del script
if __name__ == "__main__":
    inputDataBase([])