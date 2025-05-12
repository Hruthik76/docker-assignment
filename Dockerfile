FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]

