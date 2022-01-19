from src.main.scripts.objects.Cleaner import Cleaner
import src.main.scripts.functions.logger as loggerFunc
import pandas as pd

# Creamos el logger
logger = loggerFunc.getLogger("CleanerCsv")


class CleanerCsv(Cleaner):

    # Constructor
    def __init__(self, filePath):

        # Inicializamos la clase padre
        Cleaner.__init__(self, str(filePath))

    # Métodos
    def getFileDf(self, sep=','):
        try:
            return pd.read_csv(str(self._filePath), sep=sep)
        except Exception as e:
            logger.error("Error retornando fichero csv : " + str(e))
            return -1
