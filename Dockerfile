FROM python:3.8
ENV PYTHONBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip setuptools
COPY ./userManagerApp/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./userManagerApp/ /usr/src/app/

EXPOSE 8000