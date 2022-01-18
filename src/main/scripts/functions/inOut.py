import configparser
import inspect
import sys

import src.main.scripts.functions.logger as loggerFunc


# -----------------------------------------------------------------------------------------------
# DESC:
#   Configura el config parser (Para leer y escribir en el fichero config.ini)
#   Configuramos el logger
# Params:
#   No tiene
# Return:
#   Nada
# Llamar a esta función solo desde el main.py

def setConfig(logger_level=30):
    # Preparamos el logger
    loggerFunc.setLoggerConfig()

    # Preparamos el configParser
    try:
        # Control para que se llame a la función únicamente desde main.py
        if inspect.stack()[1][1].split("/")[-1] != "main.py":
            raise Exception("You can only call this method from main.py")

        # Preparamos el configParser
        conf = configparser.ConfigParser()
        # Leemos el fichero config.ini
        conf.read(sys.path[1] + "/config.ini")
        # Escribimos en el configParser (No en el fichero)
        conf['DEFAULT']['root_path'] = sys.path[1]
        conf['DEFAULT']['config_path'] = conf['DEFAULT']['root_path'] + "/config.ini"
        conf['DEFAULT']['logger_level'] = str(logger_level)  # Nivel del logger por defecto

        # Creamos una key nueva para guardar datos sobre los ficheros
        conf['raw_files'] = {}
        conf['raw_files']["raw_files_path"] = conf['DEFAULT']['root_path'] + "\\src\\main\\res\\raw"
        conf['raw_files']["edadmedia_munic_csv"] = conf['raw_files']["raw_files_path"] + \
                                                   "\\edadMedia_sexo_municipio.csv"
        conf['raw_files']["paro_sem1_2019_xls"] = conf['raw_files']["raw_files_path"] + \
                                                  "\\Paro_por_municipios_primer_semestre_2019_xls.xls"
        conf['raw_files']["paro_sem2_2019_xls"] = conf['raw_files']["raw_files_path"] + \
                                                  "\\Paro_por_municipios_segundo_semestre_2019_xls.xls"
        conf['raw_files']["paro_sem1_2020_xls"] = conf['raw_files']["raw_files_path"] + \
                                                  "\\Paro_por_municipios_primer_semestre_2020_xls.xls"
        conf['raw_files']["paro_sem2_2020_xls"] = conf['raw_files']["raw_files_path"] + \
                                                  "\\Paro_por_municipios_segundo_semestre_2020_xls.xls"

        # Sobreescribimos el fichero y guardamos la info nueva
        with open(conf['DEFAULT']['config_path'], 'w') as configfile:
            conf.write(configfile)
    except Exception as e:
        # Este error lo mostramos por pantalla ya que el logger no está configurado.
        print("Error en setConfig(): " + str(e))
        pass

# -----------------------------------------------------------------------------------------------
# DESC:
#   Devuelve el configParser para que se pueda leer el fichero config.ini cómodamente
# Params:
#   No tiene
# Return:
#   configParser si ha ido bien, False si ha ido mal


def readConfig():
    try:
        # Preparamos el configParser
        conf = configparser.ConfigParser()
        # Leemos el fichero config.ini
        conf.read(sys.path[1] + "/config.ini")
        # Retornamos el configParser
        return conf
    except Exception as e:
        logger = loggerFunc.getLogger("inOutFunctions")
        logger.error(str(e))
        return False

# -----------------------------------------------------------------------------------------------
