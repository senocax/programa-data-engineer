import logging.config
from os import path
from CalcularEdad import Empleados

if __name__=='__main__':
   
    # ----- Config. logging ------
    log_file_path = path.join(path.dirname(path.abspath('log_file_config.conf')), 'log_file_config.conf')
    logging.config.fileConfig(log_file_path)
    logger_main = logging.getLogger('main')
    logger_functions = logging.getLogger('functions')
    # -----End Config. logging ------

    try:
        logger_main.info('...Inciando ejecución...')

        empleado= Empleados("Juan","Perez","01/10/1980", "12333982")
        logger_functions.info(f'{empleado.calcular_edad()}')

        logger_functions.info(f'Hola, soy {empleado.nombre}  {empleado.apellido}. Nací el {empleado.fecha_nacimiento} y mi DNI es {empleado.nro_DNI}')

    except OSError as e:
        logger_main.error('...Error en ejecucion ...')
    finally:
        logger_main.info('...Fin de ejecución...')
