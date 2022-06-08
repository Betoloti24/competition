# IMPORTACION DE LIBRERIAS
import os

# DECLARACION DE FUNCIONES
# Funcion para limpiar pantalla
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")