import src.main.scripts.functions.logger as loggerFunc
import src.main.scripts.functions.postgresql as postgresFunc

# Creamos el logger
logger = loggerFunc.getLogger("ExtractFunc")


# Función para cargar los datos del csv a la capa raw de postgresql
def load_edadMedia_munic_csv(clCsv, df):
    try:
        logger.info("Cargando datos de " + str(clCsv._filePath).split("\\")[-1] + " en bd schema RAW ....")

        logger.debug("Preparándo conexión con la bd ....")
        conn = postgresFunc.getConn()
        logger.debug("Conexión establecida.")

        logger.debug("Hacemos una copia del dataframe, para no trabajar sobre una referencia")
        df = df.copy()

        logger.debug("Cambiamos los nombres de las columnas para que coincida con los campos de la bd")
        df = df.rename(columns={'Municipios': 'Municipio'})
        logger.debug("Columnas actualizadas correctamente.")

        logger.debug("Cargando datos en la bd ....")
        postgresFunc.db_execute_batch(conn, df, '"RAW".edad_media_sexo_municipio')
        logger.info("Datos cargados correctamente")

        logger.debug("Datos cargados.")
    except Exception as e:
        txt = "Error cargando los datos los datos de '" + \
              str(clCsv._filePath).split("\\")[-1] + "'. " + str(e) + ". Omitiendo carga...."
        logger.error(txt)
        return False

def load_paro_munic_xls(clXls, df):
    try:
        fileName = str(clXls._filePath).split("\\")[-1]
        logger.info("Cargando datos de " + fileName + " en bd schema RAW ....")

        logger.debug("Preparándo conexión con la bd ....")
        conn = postgresFunc.getConn()
        logger.debug("Conexión establecida.")

        logger.debug("Hacemos una copia del dataframe, para no trabajar sobre una referencia")
        df = df.copy()

        logger.debug("Cambiamos los nombres de las columnas para que coincida con los campos de la bd")
        df = df.rename(columns={'Código mes ': 'codigo_mes', 'Código de CA':'codigo_ca',
                                'Comunidad Autónoma':'comunidad_autonoma', 'Codigo Provincia':'codigo_provincia',
                                'Codigo Municipio':'codigo_municipio', 'total Paro Registrado':'total_paro_registrado',
                                'Paro hombre edad < 25':'paro_hombre_edad_menor_25',
                                'Paro hombre edad 25 -45 ':'paro_hombre_edad_entre_25_45',
                                'Paro hombre edad >=45':'paro_hombre_edad_mayor_45',
                                'Paro mujer edad < 25': 'paro_mujer_edad_menor_25',
                                'Paro mujer edad 25 -45 ': 'paro_mujer_edad_entre_25_45',
                                'Paro mujer edad >=45': 'paro_mujer_edad_mayor_45',
                                'Paro Agricultura':'paro_agricultura',
                                'Paro Industria':'paro_industria',
                                'Paro Construcción':'paro_construccion',
                                'Paro Servicios':'paro_servicios',
                                'Paro Sin empleo Anterior':'paro_sin_empleo_anterior',
                                })
        logger.debug("Columnas actualizadas correctamente.")

        # Sacamos el nombrede la tabla
        anio = str(fileName.split("_")[-2])
        sem = str(fileName.split("_")[-4])
        if sem == 'primer':
            sem = 'semestre1'
        elif sem == 'segundo':
            sem = 'semestre2'

        tableName = '"RAW".paro_municipio_' + str(sem) + '_' + str(anio)

        logger.debug("Cargando datos en la bd ....")
        postgresFunc.db_execute_batch(conn, df, str(tableName), page_size=500)
        logger.info("Datos cargados correctamente")

    except Exception as e:
        txt = "Error cargando los datos los datos de '" + \
              str(clXls._filePath).split("\\")[-1] + "'. " + str(e) + ". Omitiendo carga...."
        logger.error(txt)
        return False