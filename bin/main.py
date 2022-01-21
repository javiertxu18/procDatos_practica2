import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc
import src.main.scripts.functions.orig_to_raw.jobs as jobsRawFunc
import src.main.scripts.functions.raw_to_op.jobs as jobsOperationalFunc


def main():
    inOutFunc.setConfig()

    # Creamos el logger
    logger = loggerFunc.getLogger("main")

    logger.debug("Inicio programa.")

    print("\nPráctica 2\n\nETL de 'edadMedia_sexo_municipio.csv' a PostgreSQL capa RAW")
    jobsRawFunc.jobEdadMediaMunic()
    print("\nETL de 'edadMedia_sexo_municipio.csv' a PostgreSQL capa RAW completado")

    print("\nETL de los xls sobre el paro a PostgreSQL capa RAW")
    jobsRawFunc.jobParoPorMunic()
    print("\nETL de los xls sobre el paro a PostgreSQL capa RAW completado")


    print("\n\nETL de tabla edad_media_sexo_municipio a capa OPERACIONAL")
    jobsOperationalFunc.jobEdadMediaMunic()
    print("\nETL de edad_media_sexo_municipio a PostgreSQL capa Operacional completado")

    print("\nETL de las tablas sobre el paro a PostgreSQL capa OPERACIONAL")
    jobsOperationalFunc.jobParoPorMunic()
    print("\nETL de las tablas sobre el paro a PostgreSQL capa OPERACIONAL completado")

    print("Fin de programa.")

    logger.debug("Fin de programa.")


if __name__ == '__main__':
    main()
