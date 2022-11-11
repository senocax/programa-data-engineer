import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

print('HOST: {HOST} -PORT: {PORT} -USER: {USER} -PWD: {PWD}'.format(HOST=os.getenv('POSTGRESQL_HOST'),
PORT=os.getenv('POSTGRESQL_PORT'),
USER=os.getenv('POSTGRESQL_USER'),
PWD=os.getenv('POSTGRESQL_PWD')))

'''from decouple import config
print('HOST: {HOST} -PORT: {PORT} -USER: {USER} -PWD: {PWD}'.format(HOST=config('POSTGRESQL_HOST'),
PORT=config('POSTGRESQL_PORT'),
USER=config('POSTGRESQL_USER'),
PWD=config('POSTGRESQL_PWD')))'''
