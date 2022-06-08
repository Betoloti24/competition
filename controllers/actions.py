## Este modulo posee todos los metodos que conforman la impresion de datos en formato de tabla

## IMPORTACION DE PAQUETES
from statistics import mean
from datetime import timedelta, time
from controllers.utils import clear_screen

## DEFINICION DE FUNCIONES
# Funcion para imprimir la tabla con los datos de todos los participantes
def printParticipants(list_participants:list) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\t DATOS DE LOS PARTICIPANTES:")
    print("\t----------------------------------------------------------------------------------------------")
    print("\t| # |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------")
    for i, participant in enumerate(list_participants):
        ## Imprimimos los datos de cada participante
        print("\t|{:3}| {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(i+1,participant["ci"], participant["name"], participant["initial_name"], participant["surname1"], participant["surname2"], participant["sex"], participant["age"], participant["time"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion que imprime la cantidad de participantes
def printTotalParticipants(list_participants:list) -> None:
    # Impresion de resultados formateados en la linea
    clear_screen()
    print(f"\n\tCANTIDAD DE PARTICIPANTES:\n\n\tSe poseen un total de {len(list_participants)} participantes registrados\n\n\t", end="")

# Funcion que imprime una tabla con la cantidad de participantes por grupo etario
def printParticipantsByGroup(list_junior:list, list_master:list, list_senior:list) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tDATOS DE LOS PARTICIPANTES POR GRUPO ETARIO:\n")
    print("\t------------------------")
    print("\t|#|  Grupo  | Cantidad |")
    print("\t------------------------")
    ## Imprimimos los datos de cada participante
    print("\t|{:1}| {:8}|{:7}   |".format(1, "Junior", len(list_junior)))
    print("\t|{:1}| {:8}|{:7}   |".format(2, "Senior", len(list_senior)))
    print("\t|{:1}| {:8}|{:7}   |".format(3, "Master", len(list_master)))
    print("\t------------------------")
    print("\t|   Total:       {:3}   |".format(len(list_junior)+len(list_senior)+len(list_master)))
    print("\t------------------------\n\n\t", end="")

# Funcion que imprime una tabla con la cantidad de participantes por sexo
def printParticipantsBySex(list_men:list, list_women:list) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tDATOS DE LOS PARTICIPANTES POR SEXO:\n")
    print("\t-------------------------")
    print("\t|#|   Sexo   | Cantidad |")
    print("\t-------------------------")
    ## Imprimimos los datos de cada participante
    print("\t|{:1}| {:9}|{:7}   |".format(1, "Hombres", len(list_men)))
    print("\t|{:1}| {:9}|{:7}   |".format(2, "Mujeres", len(list_women)))
    print("\t-------------------------")
    print("\t|   Total:        {:3}   |".format(len(list_men)+len(list_women)))
    print("\t-------------------------\n\n\t", end="")

# Funcion que imprime los gananadores por grupo etario
def printWinnersByGroup(list_junior:list, list_senior:list, list_master:list) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    
    ## Imprimimos el encabezado
    print("\n\tGANADORES POR GRUPO ETARIO:\n")
    
    ## Imprimimos a los ganadores por grupo etario
    print("\t----------------------------------------------------------------------------------------------------")
    print("\t|  Grupo  |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t----------------------------------------------------------------------------------------------------")
   
    ## Imprimimos los datos del ganador junior
    print("\t| Junior  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(list_junior[0]["ci"], list_junior[0]["name"], list_junior[0]["initial_name"], list_junior[0]["surname1"], list_junior[0]["surname2"], list_junior[0]["sex"], list_junior[0]["age"], list_junior[0]["time"].strftime("%H:%M:%S")))
    ## Imprimimos los datos del ganador senior
    print("\t| Senior  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(list_senior[0]["ci"], list_senior[0]["name"], list_senior[0]["initial_name"], list_senior[0]["surname1"], list_senior[0]["surname2"], list_senior[0]["sex"], list_senior[0]["age"], list_senior[0]["time"].strftime("%H:%M:%S")))
    ## Imprimimos los datos del ganador master
    print("\t| Master  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(list_master[0]["ci"], list_master[0]["name"], list_master[0]["initial_name"], list_master[0]["surname1"], list_master[0]["surname2"], list_master[0]["sex"], list_master[0]["age"], list_master[0]["time"].strftime("%H:%M:%S")))
    print("\t----------------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion para imprimir los ganadores por sexo
def printWinnersBySex(list_men:list, list_women:list) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tGANADORES POR SEXO:\n")
    ## Imprimimos a los ganadores por sexo
    print("\t------------------------------------------------------------------------------------------------------")
    print("\t|   Grupo   |  Cedula  |    Nombre    |Inicial| 1er Apellido |   2do Apellido   |Sexo|Edad|  Tiempo  |")
    print("\t------------------------------------------------------------------------------------------------------")
    print("\t| Femenino  | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(list_women[0]["ci"], list_women[0]["name"], list_women[0]["initial_name"], list_women[0]["surname1"], list_women[0]["surname2"], list_women[0]["sex"], list_women[0]["age"], list_women[0]["time"].strftime("%H:%M:%S")))
    print("\t| Masculino | {:9}| {:13}|   {:4}| {:13}| {:17}| {:3}|{:3} | {:9}|".format(list_men[0]["ci"], list_men[0]["name"], list_men[0]["initial_name"], list_men[0]["surname1"], list_men[0]["surname2"], list_men[0]["sex"], list_men[0]["age"], list_men[0]["time"].strftime("%H:%M:%S")))
    print("\t------------------------------------------------------------------------------------------------------\n\n\t", end="")

# Funcion para imprimir los ganadores por etario y sexo
def printWinnersByGroupSex(list_junior:list, list_senior:list, list_master:list) -> None:
    # Declaracion de variables
    ## Ganadores de mujeres y de hombres por grupo etario
    list_junior_women = [participant for participant in list_junior if (participant["sex"] == "F")]
    list_junior_men = [participant for participant in list_junior if (participant["sex"] == "M")]
    list_senior_women = [participant for participant in list_senior if (participant["sex"] == "F")]
    list_senior_men = [participant for participant in list_senior if (participant["sex"] == "M")]
    list_master_women = [participant for participant in list_master if (participant["sex"] == "F")]
    list_master_men = [participant for participant in list_master if (participant["sex"] == "M")]
    ## Evaluamos si existe al menos un registro en cada lista, si no, creamos un dict con claves que posee en valor N/A
    winner_junior_women = list_junior_women[0] if (len(list_junior_women) != 0) else {"name": "N/A", "surname1": "", "time": "N/A"} 
    winner_junior_men = list_junior_men[0] if (len(list_junior_men) != 0) else {"name": "N/A", "surname1": "", "time": "N/A"} 
    winner_senior_women = list_senior_women[0] if (len(list_senior_women) != 0) else {"name": "N/A", "surname1": "", "time": "N/A"} 
    winner_senior_men = list_senior_men[0] if (len(list_senior_men) != 0) else {"name": "N/A", "surname1": "", "time": "N/A"} 
    winner_master_women = list_master_women[0] if (len(list_master_women) != 0) else {"name": "N/A", "surname1": "", "time": "N/A"} 
    winner_master_men = list_master_men[0] if (len(list_master_men) != 0) else {"name": "N/A", "surname1": "", "time": "N/A"}
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tGANADORES POR DE CADA GRUPO ETARIO POR SEXO:\n")
    # Impresion de resultados formateados en tabla
    print("\t         |-------------------------------------|-------------------------------------|")
    print("\t         |*              Mujeres              *|*              Hombres              *|")
    print("\t         |-------------------------------------|-------------------------------------|")
    print("\t         |*  Nombre y Apellido  *|*   Tiempo  *|*  Nombre y Apellido  *|*   Tiempo  *|")
    print("\t|--------|-----------------------|-------------|-----------------------|-------------|")
    print("\t| Junior |*     {:>15} *|*{:>10} *|*  {:>18} *|*{:>10} *|".format(winner_junior_women["name"] + winner_junior_women["surname1"], str(winner_junior_women["time"]), winner_junior_men["name"] + winner_junior_men["surname1"], str(winner_junior_men["time"])))
    print("\t| Senior |*     {:>15} *|*{:>10} *|*  {:>18} *|*{:>10} *|".format(winner_senior_women["name"] + winner_senior_women["surname1"], str(winner_senior_women["time"]), winner_senior_men["name"] + winner_senior_men["surname1"], str(winner_senior_men["time"])))
    print("\t| Master |*     {:>15} *|*{:>10} *|*  {:>18} *|*{:>10} *|".format(winner_master_women["name"] + winner_master_women["surname1"], str(winner_master_women["time"]), winner_master_men["name"] + winner_master_men["surname1"], str(winner_master_men["time"])))
    print("\t|--------|-----------------------|-------------|-----------------------|-------------|\n\n\t", end="")

# Funcion para imprimir al ganador general
def printWinner(winner:dict) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tGANADOR GENERAL:\n")
    ## Imprimimos los datos del ganador
    print("\tEntre todos los participantes, el que posee el mejor tiempo es:\n")
    print("\t  Cedula de Identidad: {}, Nombre: {}, Inicial del 2do Nombre: {}, 1er Apellido: {}, 2do Apellido: {}, Sexo: {}, Edad: {} años de edad, Tiempo Record: {}\n\n\t".format(winner["ci"], winner["name"], winner["initial_name"], winner["surname1"], winner["surname2"], winner["sex"], winner["age"], winner["time"].strftime("%H:%M:%S")), end="")

# Funcion para imprimir el histograma de participantes por grupo etario
def printHistogram(list_junior:list, list_senior:list, list_master:list) -> None:
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tHISTOGRAMA DE PARTICIPANTES POR GRUPO ETARIO:\n")
    ## Imprimimos los datos de cada participante
    print(f"\tJunior({len(list_junior):>3}): ", "| ", "*" * len(list_junior))
    print(f"\tSenior({len(list_senior):>3}): ", "| ", "*" * len(list_senior))
    print(f"\tMaster({len(list_master):>3}): ", "| ", "*" * len(list_master), "\n\n\t", end="")

# Funcion para mostrar el promedio de tiempo de los grupos etarios y el sexo
def printAverageTime(list_junior:list, list_senior:list, list_master:list) -> None:
    # Declaracion de variables
    ## Funciones lambda
    f_seconds = lambda ptime: ptime['time'].hour*3600 + ptime['time'].minute*60 + ptime['time'].second
    ## Listas de mujeres y de hombres por grupo etario
    list_junior_women = [participant for participant in list_junior if (participant["sex"] == "F")]
    list_junior_men = [participant for participant in list_junior if (participant["sex"] == "M")]
    list_senior_women = [participant for participant in list_senior if (participant["sex"] == "F")]
    list_senior_men = [participant for participant in list_senior if (participant["sex"] == "M")]
    list_master_women = [participant for participant in list_master if (participant["sex"] == "F")]
    list_master_men = [participant for participant in list_master if (participant["sex"] == "M")]
    ## Evaluamos si existe al menos un registro en cada lista, si no, creamos un dict con clave time igual a 00:00:00
    list_junior_women = list_junior_women if (len(list_junior_women) != 0) else [{"time": time(second=0)}]
    list_junior_men = list_junior_men if (len(list_junior_men) != 0) else [{"time": time(second=0)}] 
    list_senior_women = list_senior_women if (len(list_senior_women) != 0) else [{"time": time(second=0)}]
    list_senior_men = list_senior_men if (len(list_senior_men) != 0) else [{"time": time(seconds=0)}] 
    list_master_women = list_master_women if (len(list_master_women) != 0) else [{"time": time(seconds=0)}] 
    list_master_men = list_master_men if (len(list_master_men) != 0) else [{"time": time(second=0)}]
    # Impresion de resultados formateados en tabla
    clear_screen()
    ## Imprimimos el encabezado
    print("\n\tPROMEDIO DE TIEMPO POR CADA GRUPO ETARIO POR SEXO:\n")
    ## Imprimimos los datos de cada participante -> determinamos los segundos con la funcion f_seconds, determinamos el promedio en segundos y creamos un obj de tipo time a partir de los segundos otenidos
    print("\t         |------------------|------------------|")
    print("\t         |* Tiempo Mujeres *|* Tiempo Hombres *|")
    print("\t|--------|------------------|------------------|")
    print("\t| Junior |      {:>10}  |      {:>10}  |".format(str(timedelta(seconds=int(mean(list(map(f_seconds, list_junior_women)))))), str(timedelta(seconds=int(mean(list(map(f_seconds, list_junior_men))))))))
    print("\t| Senior |      {:>10}  |      {:>10}  |".format(str(timedelta(seconds=int(mean(list(map(f_seconds, list_senior_women)))))), str(timedelta(seconds=int(mean(list(map(f_seconds, list_senior_men))))))))
    print("\t| Master |      {:>10}  |      {:>10}  |".format(str(timedelta(seconds=int(mean(list(map(f_seconds, list_master_women)))))), str(timedelta(seconds=int(mean(list(map(f_seconds, list_master_men))))))))
    print("\t|--------|------------------|------------------|\n\n\t", end="")