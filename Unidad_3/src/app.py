import logging

logger= logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

c_handler= logging.StreamHandler()
f_handler= logging.FileHandler('task3.log')

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

c_format=logging.Formatter('%(asctime)s %(message)s')
f_format= logging.Formatter('%(asctime)s %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]

for item in fruits:
    try:
        logger.info(f'conversion exitosa: {item} ---> {item.lower()}') 
    except:
        logger.error(f'conversion fallida: {item}')