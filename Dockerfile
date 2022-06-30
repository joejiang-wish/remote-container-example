FROM python:2.7-buster
WORKDIR /root/app
COPY requirements.txt /root/app/requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "/root/app/server.py"]
