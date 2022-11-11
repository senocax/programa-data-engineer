import logging.config
from os import path
from functions import longitud_palabras

if __name__=='__main__':

    # ----- Configución logging ------
    log_file_path = path.join(path.dirname(path.abspath('log_file_config.conf')), 'log_file_config.conf')
    logging.config.fileConfig(log_file_path)
    logger_main = logging.getLogger('main')
    logger_functions = logging.getLogger('functions')
    # -----Fin Configución logging ------

    try:
        logger_main.info('...Inciando ejecución...')
        lista_inicial = ["perro", "elefante", "dragón"]
        logger_functions.info(f'{longitud_palabras(lista_inicial)}')
    except OSError as e:
        logger_main.error('...Error en ejecucion ...')
    finally:
        logger_main.info('...Fin de ejecución...')

