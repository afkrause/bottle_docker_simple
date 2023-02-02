# syntax=docker/dockerfile:1
FROM debian:latest
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-bottle
#WORKDIR /app
COPY bottle_simple.py .
EXPOSE 80
CMD ["python3", "bottle_simple.py"]
