FROM python:3.8
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN apt-get update -y && \
apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app