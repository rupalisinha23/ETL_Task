FROM python:3.7
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    postgresql python-psycopg2 libpq-dev

COPY ./requirements.txt /requirements.txt

# copy current work dir
WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

# run scripts
ENTRYPOINT ["/bin/bash"]

CMD ["start.sh"]
