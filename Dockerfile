FROM debian:latest


WORKDIR /app

COPY . .

RUN apt-get update  && apt-get install -y python3 python3-pip



CMD ["python3", "app.py"]

