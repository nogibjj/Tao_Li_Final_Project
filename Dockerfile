FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "app.py" ]

ENTRYPOINT ["python"]