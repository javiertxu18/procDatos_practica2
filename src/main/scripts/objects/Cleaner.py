
class Cleaner:

    # constructor
    def __init__(self, filePath):
        self._filePath = str(filePath)

    # Métodos

    # Para retornar la ruta del archivo
    def getFilePath(self):
        return self._filePath
