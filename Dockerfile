FROM python:3.8

RUN mkdir -p /app

COPY . app.py requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "app.py" ]

ENTRYPOINT [ "python" ]