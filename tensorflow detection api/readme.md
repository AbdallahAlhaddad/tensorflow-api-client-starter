### tested on python 3.8

1. install virtualenv

```bash
pip install virtualenv
```

2. create a virtual environment:

```bash
virtualenv venv
```

3. activate the created virtualenv:

- windows:

```bash
venv\Scripts\activate
```

- linux & mac:

```bash
source venv/bin/activate
```

4. install dependencies in the created virtual env using pip:

```bash
pip install uvicorn fastapi numpy tensorflow pillow python-multipart
```

3. run server:

- windows:

```bash
py .\server.py
```

- linux:

```bash
python3 server.py
```
