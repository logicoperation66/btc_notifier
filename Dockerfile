FROM ubuntu:latest
LABEL authors="adam.wawrzyniak"

ENTRYPOINT ["top", "-b"]