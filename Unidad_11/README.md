# Testing II - Practical

Generate sequence diagram test with docs-from-test library and write to file testing.txt.
## Deploy

Create virtual environment (venv)
```
python -m venv path\to\myenv
```
● Install library
```
pip install docs-from-test
```

● Run test
```
python tests/test.py
```
Sequence Diagram generate:
![Alt text](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5hZGQ6IGNhbGxzIHgzCiAgYWRkLS0+PnN0YXJ0OiByZXR1cm5zIGZsb2F0CiAgc3RhcnQtPj5zdWJ0cmFjdDogY2FsbHMgeDMKICBzdWJ0cmFjdC0tPj5zdGFydDogcmV0dXJucyBmbG9hdAogIHN0YXJ0LT4+bXVsdGlwbHk6IGNhbGxzIHgzCiAgbXVsdGlwbHktLT4+c3RhcnQ6IHJldHVybnMgZmxvYXQKICBzdGFydC0+PmRpdmlkZTogY2FsbHMgeDQKICBkaXZpZGUtLT4+c3RhcnQ6IHJldHVybnMgZmxvYXQK)
