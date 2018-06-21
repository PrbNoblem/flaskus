FROM python:3.6-alpine

# creates a user inside the docker
RUN adduser -D microblog

# change dir in the docker
WORKDIR /home/microblog

# copy req. file from here to there
COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn


COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./

RUN chmod +x boot.sh

# Env. variable for the docker. Required to use the flask command.
ENV FLASK_APP microblog.py

# Set ownerchip recursively to the new microblog user
RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000

# command that defines what should be executed when the container is started.
ENTRYPOINT ["./boot.sh"]