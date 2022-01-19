import numpy as np
import pandas as pd
import src.main.scripts.functions.logger as loggerFunc

# Creamos el logger
logger = loggerFunc.getLogger("TransformFunc")


def transform_edadMedia_munic_csv(df, clCsv):
    try:
        logger.debug("Transformando los datos del fichero '" + str(clCsv._filePath).split('\\')[-1] + "'....")

        logger.debug("Hacemos una copia del dataframe, para no trabajar sobre una referencia")
        df = df.copy()

        logger.debug("Limpliamos las líneas que tengan todos los campos vacíos.")
        ant = int(len(df))
        df.dropna(axis=0, how='all', inplace=True)
        logger.debug(f"Se han borrado {ant - int(len(df))} registros por estar la línea completa vacía.")

        logger.debug("Separamos la columna municipios por cp y nombre.")
        df[['cp', 'name']] = df["Municipios"].str.split(" ", 1, expand=True)
        df = df[['cp', 'name', 'Sexo', 'Periodo', 'Total']]
        logger.debug("Ok.")

        logger.debug("Tratando campos nan....")
        nanDf = df[df.isna().any(axis=1)]
        logger.debug(f"{len(nanDf)} líneas con algún nan.")

        logger.debug("Tratando campos nan en la columna de 'Total'")
        logger.debug("Casteamos la columna a tipo float")
        df["Total"] = df["Total"].str.replace(",", ".")
        df["Total"] = pd.to_numeric(df["Total"], downcast="float")

        logger.debug("Sacamos la media de la columna con la que vamos a rellenar los nan")
        logger.debug("Hacemos una copia del dataframe y la guardamos en temp.")
        temp = df.copy()
        logger.debug("Borramos todas las filas que tangan algún nan.")
        temp = temp.dropna(axis=0, how='any')
        logger.debug("Guardamos la media total de la columna en una variable")
        mediaTotal = np.mean(temp["Total"].tolist())

        logger.debug("Actualizamos todos los nan de la columna 'Total' por la media obtenida.")
        df["Total"] = df["Total"].fillna(mediaTotal)
        logger.debug("Ok.")

        logger.debug("Limpiamos el resto de nan si los hubiera")
        df.dropna(axis=0, how='any', inplace=True)
        logger.debug("Ok.")

        logger.debug("Datos transformados correctamente")
        return True
    except Exception as e:
        logger.error("Error transformando los datos de 'src/main/res/raw/edadMedia_sexo_municipio.csv'. " + str(e))
        return False


def transform_paro_munic_xls(df, cl):
    logger.debug("Transformando los datos del fichero '" + str(cl._filePath).split('\\')[-1] + "' ....")

    logger.debug("Hacemos una copia del dataframe, para no trabajar sobre una referencia")
    df = df.copy()

    logger.debug("Limpliamos las líneas que tengan todos los campos vacíos.")
    ant = int(len(df))
    df.dropna(axis=0, how='all', inplace=True)
    logger.debug(f"Se han borrado {ant - int(len(df))} registros por estar la línea completa vacía.")

    logger.debug("Si la columna 'Codigo Municipio' está vacía, omitimos toda la línea.")
    ant = int(len(df))
    df = df[df['Codigo Municipio'].notna()]
    logger.debug(f"Se han borrado {ant - int(len(df))} registros por estar la columna vacía.")

    logger.debug("Si las columnas siguientes a 'total Paro Registrado'(no incluida)"
                 " tienen valores vacíos, rellenar con 0.")
    df.loc[:, 'Paro hombre edad < 25':] = df.loc[:, 'Paro hombre edad < 25':].fillna(0)
    logger.debug("Ok.")

    logger.debug("Si las columnas siguientes a 'total Paro Registrado'(no incluida)")


    logger.debug("Rellenamos la columna 'total Paro Registrado' con la suma de las columnas siguientes.")

    # Creamos una función local para el apply del df
    def calc_sumTotalParo(x, dfLoc):
        return dfLoc.sum(axis=1)

    df.loc[:0, 'total Paro Registrado'] = df.apply(
        calc_sumTotalParo, dfLoc=df.loc[:, 'Paro hombre edad < 25':'Paro mujer edad >=45'])
    logger.debug("Ok")


    logger.debug("Limpiamos el resto de nan si los hubiera")
    df.dropna(axis=0, how='any', inplace=True)
    logger.debug("Ok.")

    logger.debug("Parseamos a int las col siguientes a 'total Paro Registrado'(incluido) ....")
    df.loc[:,'total Paro Registrado':] = df.loc[:,'total Paro Registrado':].applymap(int)
    logger.debug("Ok.")
