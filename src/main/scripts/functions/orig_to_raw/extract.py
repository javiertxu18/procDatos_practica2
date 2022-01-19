import src.main.scripts.functions.logger as loggerFunc

# Creamos el logger
logger = loggerFunc.getLogger("ExtractFunc")


def extract_edadMedia_munic_csv(clCsv):
    try:
        logger.debug("Extrayendo datos del fichero '" + str(clCsv._filePath).split('\\')[-1] + "'....")
        dev = clCsv.getFileDf(";")
        logger.debug("Datos extraídos correctamente")
        return dev
    except Exception as e:
        logger.error("Error extrayendo datos de 'src/main/res/raw/edadMedia_sexo_municipio.csv'. " + str(e))
        return False


def extract_paro_munic_xls(clXls):
    try:
        logger.debug("Extrayendo datos del fichero '" + str(clXls._filePath).split('\\')[-1] + "'....")
        dev = clXls.getFileDf(header=1)
        logger.debug("Datos extraídos correctamente")
        return dev
    except Exception as e:
        logger.error("Error extrayendo datos de 'src/main/res/raw/edadMedia_sexo_municipio.csv'. " + str(e))
        return False
