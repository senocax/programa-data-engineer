
# Comments in Python - Docstrings - Practical
Using Docstring and generating documentation with Sphinx.
## Deploy

● Create virtual environment (venv)
```
python -m venv path\to\myenv
```
● Install requirements.txt 
```
pip install requirements.txt 
```
● Practical Install Sphinx
```
pip install -U sphinx
```
● Create .srt files to the docs directory
```
sphinx-apidoc -o docs source
```

● Create Sphinx documentation
```
make html
```

● Run main
```
python source/main.py
```

● HTML documentation generate by Sphinx (directory /_build/html/index.html)

![Alt text](https://res.cloudinary.com/dimgzkmps/image/upload/v1668358913/sphinx_qbe37p.png)
