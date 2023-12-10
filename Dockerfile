FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME World

CMD ["unicorn", "app.py", "--host=0.0.0.0", "--port=5000"]