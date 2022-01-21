import src.main.scripts.functions.inOut as inOutFunc

config = inOutFunc.readConfig()


class Cleaner:

    # constructor
    def __init__(self, filePath):
        self._filePath = str(filePath)

    # Métodos

    # Para retornar la ruta del archivo
    def getFilePath(self):
        return self._filePath

    # Para comprobar la conexión con la bd
    def isConnDB(self):
        print("fghdfhg")
        return True
