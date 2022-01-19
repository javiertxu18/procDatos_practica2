from src.main.scripts.objects.Cleaner import Cleaner
import src.main.scripts.functions.logger as loggerFunc
import pandas as pd

# Creamos el logger
logger = loggerFunc.getLogger("CleanerXls")


class CleanerXls(Cleaner):

    # Constructor
    def __init__(self, filePath):

        # Inicializamos la clase padre
        Cleaner.__init__(self, str(filePath))

    # Métodos
    def getFileDf(self, header=0):
        try:
            return pd.read_excel(str(self._filePath), header=header)
        except Exception as e:
            logger.error("Error retornando fichero xls : " + str(e))
            return -1
