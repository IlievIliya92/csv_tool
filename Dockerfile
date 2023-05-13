FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
MAINTAINER "Iliya Iliev"

#Install git
RUN apt-get update && \
     apt-get install --no-install-recommends --no-install-suggests -y git python3 python3-pip python-is-python3 && \
     pip install pytest

# Install pkg
RUN mkdir /home/csv_tool && \
     cd /home/csv_tool && \
     git clone https://github.com/IlievIliya92/csv_tool.git && \
     cd csv_tool && \
     python setup.py build && \
     python setup.py install

RUN cd /home/csv_tool/csv_tool && \
     pytest tests

#Set working directory
WORKDIR /home/csv_tool/
CMD /bin/bash
