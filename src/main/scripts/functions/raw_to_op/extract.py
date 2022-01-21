import src.main.scripts.functions.logger as loggerFunc
import src.main.scripts.functions.postgresql as postgresqlFunc

# Creamos el logger
logger = loggerFunc.getLogger("ExtractFunc")

# Función para la extracción de csv
def extract_edadMedia_munic_csv(clCsv):
    try:
        return postgresqlFunc.getFromDb('"RAW".edad_media_sexo_municipio')
    except Exception as e:
        logger.error("Error extrayendo datos de 'src/main/res/raw/edadMedia_sexo_municipio.csv'. " + str(e))
        return False

# Función para la extracción de xls
def extract_paro_munic_xls(clXls):
    try:

        # Sacamos el nombre de la tabla
        fileName = str(clXls._filePath).split("\\")[-1]

        anio = str(fileName.split("_")[-2])
        sem = str(fileName.split("_")[-4])

        if sem == 'primer':
            sem = 'semestre1'
        elif sem == 'segundo':
            sem = 'semestre2'

        tableName = '"RAW".paro_municipio_' + str(sem) + '_' + str(anio)

        return postgresqlFunc.getFromDb(tableName)
        return dev
    except Exception as e:
        logger.error("Error extrayendo datos de 'src/main/res/raw/edadMedia_sexo_municipio.csv'. " + str(e))
        return False