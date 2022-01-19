import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc
import src.main.scripts.functions.jobs as jobsFunc


def main():
    inOutFunc.setConfig()

    # Creamos el logger
    logger = loggerFunc.getLogger("main")

    # Creamos el config para poder leer el config.ini
    config = inOutFunc.readConfig()

    logger.debug("Inicio programa.")

    print("\nPráctica 2\n\nETL de 'edadMedia_sexo_municipio.csv' a PostgreSQL")
    jobsFunc.jobEdadMediaMunic()
    print("Ok")

    print("\n\nETL de los xls sobre el paro a PostgreSQL")
    jobsFunc.jobParoPorMunic()
    print("Ok")

    logger.debug("Fin de programa.")


if __name__ == '__main__':
    main()
