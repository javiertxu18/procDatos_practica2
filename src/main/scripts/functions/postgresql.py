import pandas
import psycopg2
import psycopg2.extras as extras
import pandas.io.sql as sqlio

import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc

from multipledispatch import dispatch

# No borrar las próximas 3 líneas, sino da error ah hacer el load
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


# -----------------------------------------------------------------------------------------------
# DESC:
#   Comprueba si la conn a la bd existe de verdad
# Params:
#   No tiene
# Return:
#   Retorna la connexión

def getConn():
    try:
        # Preparamos el config
        conf = inOutFunc.readConfig()
        # Comprobamos conn
        conn = psycopg2.connect(database=conf['postgresql']['db'],
                                user=conf['postgresql']['user'],
                                password=conf['postgresql']['passwd'],
                                host=conf['postgresql']['host'],
                                port=int(conf['postgresql']['port']))

        return conn
    except Exception as e:
        raise Exception(
            f"\n\n\tError al conectar con postgresql({conf['postgresql']['host']}:{conf['postgresql']['port']})"
            f" a la base de datos '{conf['postgresql']['db']}' con usuario '{conf['postgresql']['user']}'."
            f"\n\tConfigurar parámetros de conexión en el fichero config.ini"
            f"\n\tPara más información mirar el fichero .log"
            f"Error: {str(e)}")
        pass


# -----------------------------------------------------------------------------------------------
# DESC:
#   Carga los datos de un dataframe en postgreSql. Este método es más rápido que hacer inserts de una en una.
# Params:
#   conn: Conexión a bd
# Return:
#   Retorna True si ha ido bien, False si ha habido algún error

@dispatch(object, pandas.DataFrame, str, page_size=int)
def db_execute_batch(conn, df, tableName, page_size=100):
    # Preparamos el logger
    logger = loggerFunc.getLogger("postgresql")

    logger.debug("Ejecutando batch a PostgreSQL ....")

    # Guardamos la info del dataframe a tupla
    tuples = [tuple(x) for x in df.to_numpy()]
    # Sacamos las columnas a un string separado por comas
    lstCol = list(df.columns)
    cols = ','.join(lstCol)
    # Preparamos la query
    query = f"INSERT INTO %s(%s) VALUES("
    for x in range(len(df.columns) - 1):
        query += f"%%s,"
    query += f"%%s)"
    query = query % (tableName, cols)

    # Creamos el cursor
    cursor = conn.cursor()
    try:
        extras.execute_batch(cursor, query, tuples, page_size)
        conn.commit()

        cursor.close()
        conn.close()

        logger.debug("Batch ejecutado correctamente.")

        return True

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return False


# -----------------------------------------------------------------------------------------------
# DESC:
#   Extrae los datos de la tabla insertada por parámetros y los devuelve en un df
# Params:
#   tableName: Nombre de la tabla objetivo (esquema incluído)
# Return:
#   Retorna el dataframe si todo ha ido bien

@dispatch(str)
def getFromDb(tableName):
    # Preparamos el logger
    logger = loggerFunc.getLogger("postgresql")

    try:
        conn = getConn()
        sql = "select * from " + tableName
        return sqlio.read_sql_query(sql, conn)
    except Exception as e:
        logger.error("Error: " + str(e))
        return False

# -----------------------------------------------------------------------------------------------
