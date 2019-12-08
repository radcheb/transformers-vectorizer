FROM python:3.6-slim

COPY . /serving/flask_app
WORKDIR /serving/flask_app

RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh

ENV TORCH_HOME="/tmp/torch"

CMD ["./start.sh"]