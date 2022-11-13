
# Database Access - Practical

Activity Access to databases through an ORM (Object Relational Mapper). 
Create, read, delete and update data, from customer table
applying SQLAlchemy in Python.

## Deploy

● Clone repository and enter the directory of the activity 16
```
git clone https://github.com/senocax/programa-data-engineer
cd Unidad_16
```
● Create database (psql)
```
CREATE DATABASE your_db_name;
```
● Create virtual environment (venv)
```
python -m venv path\to\myenv
```
● Install requirements.txt dependencies
```
pip install requirements.txt 
```
● Configure postgreSQL database in config.ini file
```
DB_NAME = you_db_name
DB_USER = you_db_user
DB_PASSWORD = you_db_password
DB_HOST = 12.0.0.1
DB_PORT = 5432

```
● Run database
```
python database.py
```
![Alt text](https://res.cloudinary.com/dimgzkmps/image/upload/v1668374685/dbase_thwlz6.png)
