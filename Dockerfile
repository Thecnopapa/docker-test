FROM debian:trixie-slim


WORKDIR /app

COPY ./app .
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y python3 python3-pip python3.13-venv

RUN python3 -m venv venv

ENV VIRTUAL_ENV ./venv                     # activating environment
ENV PATH ./venv/bin:$PATH                  # activating environment
RUN which python                         # -> /env/bin/python
# ./venv/Scripts/activate

RUN pip3 install -i 'https://test.pypi.org/simple/' -r requirements.txt

CMD ["python3", "app.py"]

