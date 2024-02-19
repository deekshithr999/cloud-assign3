From python:3.9-slim

RUN mkdir -p /home/cloud_assign
RUN mkdir -p /home/output
RUN mkdir -p /home/data
#RUN apk update && \
#    apk add --no-cache python3

WORKDIR /home
RUN python3 --version

COPY sample.py /home/cloud_assign/
COPY /IF.txt /home/data/
COPY /Limerick-1.txt /home/data/

CMD ["python", "/home/cloud_assign/sample.py"]
