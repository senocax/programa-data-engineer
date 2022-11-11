import logging.config
from os import path
from functions import open_file,line_count, word_count

#open logger config
log_file_path = path.join(path.dirname(path.abspath('log_file_config.conf')), 'log_file_config.conf')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

#create loggers
logger_main = logging.getLogger('main')
logger_functions = logging.getLogger('functions')

if __name__ == "__main__":
 
    my_file='cuento.txt'

    #try read file
    try:
        open_file(my_file)
        logger_main.info('...Leyendo el archivo...')

        # read name of file and count max line
        for k, v in line_count(open_file(my_file)).items():
            logger_functions.info(f'{k} - Cantidad de renglones: {v}')

        # count word for line
        for k, v in word_count(open_file(my_file)).items():
            logger_functions.info(f'Reglòn {k}:{v} palabras')

    except OSError as e:
        logger_main.critical('...No se puede abrir el archivo')
    finally:
        logger_main.info('...Archivo procesado...')


