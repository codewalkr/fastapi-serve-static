FROM registry.access.redhat.com/ubi9/python-312:latest

LABEL maintainer="Richard Walker"

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

WORKDIR /opt/app-root/src

COPY . /opt/app-root/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER root

RUN chown -R 1001:1001 /opt/app-root/src
RUN chmod -R 775 /opt/app-root/src

EXPOSE 8080

USER 1001

CMD python main.py
