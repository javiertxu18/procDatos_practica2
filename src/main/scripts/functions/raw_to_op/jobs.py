from src.main.scripts.objects.CleanerCsv import CleanerCsv
from src.main.scripts.objects.CleanerXls import CleanerXls

import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc

import src.main.scripts.functions.raw_to_op.extract as extractFunc
import src.main.scripts.functions.raw_to_op.transform as transformFunc
import src.main.scripts.functions.raw_to_op.load as loadFunc

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
    logger.debug("Llamamos a la función de transformación transform_edadMedia_munic_csv().")
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

    logger.debug("Llamamos a la función de extracción extract_paro_munic_xls() y creamos un dataframe por tabla.")
    print("\nIniciando extracción ....")
    lstDf = []
    for cleaner in lstCleaner:
        timeA = datetime.now()
        lstDf.append(extractFunc.extract_paro_munic_xls(cleaner))
        timeB = datetime.now() - timeA
        logger.debug(str(cleaner._filePath.split('\\')[-1]) + ", " + str(len(lstDf[len(lstDf)-1])) +
              " registros extraídos de postgresql en " + str(timeB).split(":")[2] + " segundos.")
        print(str(cleaner._filePath.split('\\')[-1]) + ", " + str(len(lstDf[len(lstDf)-1])) +
              " registros extraídos de postgresql en " + str(timeB).split(":")[2] + " segundos.")

    logger.debug("Extracción completada.")
    print("Extracción completada.")


    print("\nOmitiendo transformación por no ser necesaria.")
    logger.debug("No es necesaria una transformación de los xls de raw a operacional.")

    print("\nIniciando carga de datos ....")
    logger.debug("Preparamos las tablas de la bd operacional ....")
    loadFunc.load_operational_tables(lstDf[0])
    logger.debug("Tablas preparadas correctamente.")
    logger.debug("Llamamos a la función de carga load_paro_munic_xls().")
    for x in range(len(lstDf)):
        timeA = datetime.now()
        loadFunc.load_paro_munic_xls(lstCleaner[x], lstDf[x])
        timeB = datetime.now() - timeA
        logger.debug(str(lstCleaner[x]._filePath.split('\\')[-1]) + ", " + str(len(lstDf[x])) +
              " registros cargados en " + str(timeB).split(":")[2] + " segundos.")
        print(str(lstCleaner[x]._filePath.split('\\')[-1]) + ", " + str(len(lstDf[x])) +
              " registros cargados en " + str(timeB).split(":")[2] + " segundos.")
    logger.debug("Carga completada.")
    
    print("Carga completada.")
