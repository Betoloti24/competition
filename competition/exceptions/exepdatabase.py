## IMPORTAMOS LOS PAQUETES

## DECLARAMOS LAS EXCEPCIONES
# Excepcion de extension del archivo
class FileNotExtension(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

# Excepcion de archivo vacio
class FileEmpty(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

# Excepcion de archivo con registros incorrectos
class FileRegisterIncorrect(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message