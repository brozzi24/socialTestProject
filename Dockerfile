FROM python:3

ENV PYTHONUNBUFFERED 1
# Copy the requirements in the local dir to the image
COPY ./requirements.txt /requirements.txt
# Install requirements
RUN pip install -r /requirements.txt
# Make dir in docker image
RUN mkdir /social_app
# Switch to docker image for starting dir
WORKDIR /social_app
# Copy the social app to the dir in the docker image
COPY ./social_app /social_app





