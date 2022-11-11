# import the libraries
import logging
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
import pandas as pd


# defining DAG arguments
default_args = {
 'owner': 'Alkemy_Prisma',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}


dag = DAG(
 'DagUnidad5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)

# Tasks

@dag.task(task_id = "read_top10")
def read_top10():
    
    # ----- Completar logging ------
    logger= logging.getLogger("Dag")
    logger.setLevel(logging.DEBUG)

    c_handler= logging.StreamHandler()
    f_handler= logging.FileHandler('/home/dev/airflow/include/archivos_tmp/medals.log','w')

    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)

    c_format=logging.Formatter('%(asctime)s %(message)s')
    f_format= logging.Formatter('%(asctime)s %(message)s')

    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    # -----Fin Completar logging ------

    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"
    
    try:

        df = pd.read_csv(url)
 
        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False).head(10)
        
        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()
        # Save data frame in Excel format - Completar tu propia ubicación para guardar el archivo de salida
        to_countries_df.to_excel('/home/dev/airflow/include/archivos_tmp/top10_medals_by_country.xlsx')

        #Logging message INFO Success --- Completar
        logging.info("...Archivo procesado correctamente...")

        
    except:
        
        #Logging message ERROR Fail --- Completar
        logging.error("...Fallo procesamiento del archivo...")

 
# task pipeline
read_top10 ()

