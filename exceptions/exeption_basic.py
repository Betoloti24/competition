## IMPORTAMOS LOS PAQUETES

## DECLARAMOS LAS EXCEPCIONES
# Excepcion de opcion del menu
class OptionMenu(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

