import src.main.scripts.functions.inOut as inOutFunc
import src.main.scripts.functions.logger as loggerFunc
from src.main.scripts.objects.CleanerCsv import CleanerCsv


def main():
    inOutFunc.setConfig()

    # Creamos el logger
    logger = loggerFunc.getLogger("Main")

    # Creamos el config para poder leer el config.ini
    config = inOutFunc.readConfig()

    logger.debug("Inicio programa.")

    print("hi")

    c = CleanerCsv(config["raw_files"]["edadmedia_munic_csv"])
    print(c.getFile())

    logger.debug("Fin programa.")


if __name__ == '__main__':
    main()
