# portfolio
self tech portfolio

## local development

1. `pip install -r requirements.txt`
2. `uvicorn app:app --reload --host 0.0.0.0 --port 8080`

## Docker

1. `docker build -t portfolio .`
2. `docker run --rm -p 8080:8080 portfolio`
