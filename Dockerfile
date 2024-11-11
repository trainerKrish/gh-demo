FROM ubuntu:latest 

RUN apt update

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip3 install flask --break-system-packages
RUN pip3 install mysql-connector-python --break-system-packages

COPY app.py .
# COPY connection.py .

CMD python3 app.py
