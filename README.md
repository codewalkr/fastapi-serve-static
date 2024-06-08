# Simple FastAPI application for service static web pages.

## Clone

Clone this repo:

```
git clone https://github.com/codewalkr/fastapi-serve-static.git
```
Change into the repo directory:

```
cd fastapi-serve-static/
```

## Develop

Create Python 3 virtual environemnt:

```
python -m venv venv
```

Activate:

```
. venv/bin/activate
```

Install packages:

```
pip install -r requirements.txt 
```

Run:

```
python main.py
```

## Build

Create local container image:

```
podman build -t localhost/fastapi-serve-static:1.0.0 .
```

Run container:

```
podman run -d -p 8080:8080 --name fastapi-serve-static localhost/fastapi-serve-static:1.0.0
```

