import logging.config
from os import path
from functions import get_transport
if __name__ == '__main__':

    # ----- Config. logging ------
    log_file_path = path.join(
        path.dirname(
            path.abspath('log_file_config.conf')),
        'log_file_config.conf')
    logging.config.fileConfig(log_file_path)
    logger_main = logging.getLogger('main')
    logger_functions = logging.getLogger('functions')
    # -----End Config. logging ------

    try:
        logger_main.info('...Starting execution...')
        logger_functions.info(f'{get_transport("Welcome!")}')
    except OSError:
        logger_main.error('...Error in execution...')
    finally:
        logger_main.info('...End of execution...')
