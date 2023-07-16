FROM python:3.8-slim-buster
EXPOSE 5000
WORKDIR /python-docker
RUN pip3 install flask
COPY . .
CMD [ "python3", "-m" , "flask", "run"]