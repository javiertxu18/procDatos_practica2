import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc
import src.main.scripts.functions.orig_to_raw.jobs as jobs1Func


def main():
    inOutFunc.setConfig()

    # Creamos el logger
    logger = loggerFunc.getLogger("main")

    # Creamos el config para poder leer el config.ini
    config = inOutFunc.readConfig()

    logger.debug("Inicio programa.")

    print("\nPráctica 2\n\nETL de 'edadMedia_sexo_municipio.csv' a PostgreSQL")
    jobs1Func.jobEdadMediaMunic()
    print("ETL completado.")

    print("\n\nETL de los xls sobre el paro a PostgreSQL")
    jobs1Func.jobParoPorMunic()
    print("ETL completado.")

    logger.debug("Fin de programa.")


if __name__ == '__main__':
    main()
