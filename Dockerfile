FROM python:3.8

RUN mkdir -p /app

COPY . app.py requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "app.py" ]

ENTRYPOINT ["python"]