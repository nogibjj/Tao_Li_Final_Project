FROM python:3.8

# RUN mkdir -p /app

# COPY . app.py requirements.txt /app/

# WORKDIR /app

# RUN pip install -r requirements.txt

# EXPOSE 5000

# CMD [ "app.py" ]

# ENTRYPOINT [ "python" ]

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt

# Stage 2: Copy the necessary files to a Distroless image
FROM gcr.io/distroless/python3

COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local

WORKDIR /app

EXPOSE 5000
CMD ["python", "app.py"]