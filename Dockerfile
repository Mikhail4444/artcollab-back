FROM python:3.12-bullseye

WORKDIR /app
COPY "requirements.txt" .
RUN ["pip3", "install", "-r", "requirements.txt"]


COPY . .
ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8000