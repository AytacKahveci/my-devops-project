from python:3.9-slim-buster

WORKDIR /app

COPY ./my_app /app

RUN pip install -r requirements.txt

EXPOSE 51500

CMD ["python", "app.py"]
