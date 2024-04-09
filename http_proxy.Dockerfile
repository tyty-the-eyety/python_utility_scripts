#FROM python:latest
FROM python:3.9-slim-buster
LABEL Maintainer="Tyron Esch"
RUN pip install --upgrade pip
RUN pip install --no-cache-dir requests 
ENV LOGGING='TRUE'
ENV PROXY_HOST='https://httpbin.org/post'
WORKDIR /usr/app/src
COPY http_proxy.py ./
CMD [ "python", "-u","./http_proxy.py"]
