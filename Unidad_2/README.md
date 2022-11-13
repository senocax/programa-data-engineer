
Display environment variables on screen, using Decouple then use dotenv. 
## Deploy

Create virtual environment (venv)
```
python -m venv path\to\myenv
```
● Generate an .env file 
```
POSTGRESQL_HOST=localhost
POSTGRESQL_PORT=5432
POSTGRESQL_USER=myuser
POSTGRESQL_PWD=mypass
```
● Practical Install Decouple
```
pip install decouple-python
```
● Install Dotenv
```
pip install dotenv
```
● Run app
```
python SRC/app.py
```
