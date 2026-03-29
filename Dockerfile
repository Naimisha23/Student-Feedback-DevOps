
FROM python:3.9

WORKDIR /app

COPY app/ /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]