FROM debian:trixie-slim AS build

RUN uname -m > /arch

WORKDIR /app


COPY ./requirements.txt .

RUN apt-get update && apt-get install -y python3 python3-pip python3.13-venv

RUN apt-get clean

RUN python3 -m venv venv

ENV VIRTUAL_ENV="./venv"
ENV PATH="./venv/bin:$PATH"
RUN which python


RUN pip3 install --extra-index-url https://test.pypi.org/simple/ bioiain>=0.0.7.1.13

RUN pip3 install --extra-index-url https://download.pytorch.org/whl/cpu torch torchvision

RUN pip3 install -r requirements.txt



COPY ./app .

RUN chmod +x ./run.sh


CMD ["./run.sh"]

