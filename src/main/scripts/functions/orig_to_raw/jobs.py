from src.main.scripts.objects.CleanerCsv import CleanerCsv
from src.main.scripts.objects.CleanerXls import CleanerXls

import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc

import src.main.scripts.functions.orig_to_raw.extract as extractFunc
import src.main.scripts.functions.orig_to_raw.transform as transformFunc
import src.main.scripts.functions.orig_to_raw.load as loadFunc

from datetime import datetime

# Creamos el logger
logger = loggerFunc.getLogger("jobs")

# Creamos el config para poder leer el config.ini
config = inOutFunc.readConfig()


def jobEdadMediaMunic():
    logger.info("Iniciamos el job jobEdadMediaMunic()....")

    logger.debug("Creamos el objeto Cleaner")
    cleaner = CleanerCsv(config["raw_files"]["edadmedia_munic_csv"])

    print("\nIniciando extracción ....")
    logger.debug("Llamamos a la función de extracción extract_edadMedia_munic_csv().")
    df = extractFunc.extract_edadMedia_munic_csv(cleaner)
    print("Extracción completada.")
    logger.debug("Extracción completada.")

    print("\nIniciando transformación ....")
    logger.debug("Llamamos a la función de transformación extract_edadMedia_munic_csv().")
    df = transformFunc.transform_edadMedia_munic_csv(df, cleaner)
    print("Transformación completada.")
    logger.debug("Transformación completada.")

    print("\nIniciando carga de datos ....")
    logger.debug("Llamamos a la función de carga load_edadMedia_munic_csv().")
    loadFunc.load_edadMedia_munic_csv(cleaner, df)
    logger.debug("Carga completada.")
    print("Carga completada.")

    logger.info("Fin del job jobEdadMediaMunic().")


def jobParoPorMunic():
    logger.info("Iniciamos el job jobParoPorMunic()....")

    logger.debug("Creamos un cleaner por fichero")
    lstCleaner = []
    lstCleaner.append(CleanerXls(config["raw_files"]["paro_sem1_2019_xls"]))
    lstCleaner.append(CleanerXls(config["raw_files"]["paro_sem2_2019_xls"]))
    lstCleaner.append(CleanerXls(config["raw_files"]["paro_sem1_2020_xls"]))
    lstCleaner.append(CleanerXls(config["raw_files"]["paro_sem2_2020_xls"]))

    logger.debug("Llamamos a la función de extracción extract_paro_munic_xls() y creamos un dataframe por fichero.")
    print("\nIniciando extracción ....")
    lstDf = []
    for cleaner in lstCleaner:
        timeA = datetime.now()
        lstDf.append(extractFunc.extract_paro_munic_xls(cleaner))
        timeB = datetime.now() - timeA
        logger.debug(str(cleaner._filePath.split('\\')[-1]) + ", " + str(len(lstDf[len(lstDf)-1])) +
              " registros extraídos en " + str(timeB).split(":")[2] + " segundos.")
        print(str(cleaner._filePath.split('\\')[-1]) + ", " + str(len(lstDf[len(lstDf)-1])) +
              " registros extraídos en " + str(timeB).split(":")[2] + " segundos.")

    logger.debug("Extracción completada.")
    print("Extracción completada.")

    print("\nIniciando transformación ....")
    logger.debug("Llamamos a la función de transformación transform_paro_munic_xls() y transformamos los dataframes.")
    lstTransformedDf = []
    for x in range(len(lstDf)):
        lstTransformedDf.append(transformFunc.transform_paro_munic_xls(lstDf[x], lstCleaner[x]))
        logger.debug(str(lstCleaner[x]._filePath.split('\\')[-1]) + " transformado.")
        print(str(lstCleaner[x]._filePath.split('\\')[-1]) + " transformado.")

    logger.debug("Transformación completada.")
    print("Transformación completada.")

    print("\nIniciando carga de datos ....")
    logger.debug("Llamamos a la función de carga load_paro_munic_xls().")
    for x in range(len(lstTransformedDf)):
        timeA = datetime.now()
        loadFunc.load_paro_munic_xls(lstCleaner[x], lstTransformedDf[x])
        timeB = datetime.now() - timeA
        logger.debug(str(lstCleaner[x]._filePath.split('\\')[-1]) + ", " + str(len(lstTransformedDf[x])) +
              " registros cargados en " + str(timeB).split(":")[2] + " segundos.")
        print(str(lstCleaner[x]._filePath.split('\\')[-1]) + ", " + str(len(lstTransformedDf[x])) +
              " registros cargados en " + str(timeB).split(":")[2] + " segundos.")
    logger.debug("Carga completada.")
    print("Carga completada.")
