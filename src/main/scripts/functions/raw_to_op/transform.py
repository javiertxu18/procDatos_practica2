import pandas as pd
import src.main.scripts.functions.logger as loggerFunc

# Creamos el logger
logger = loggerFunc.getLogger("TransformFunc")

def transform_edadMedia_munic_csv(df, clCsv):

    logger.debug("Dejamos solo el cp del municipio.")
    df["municipio"] = df["municipio"].str.split(" ", 1, expand=True)
    logger.debug("Ok.")

    return df
