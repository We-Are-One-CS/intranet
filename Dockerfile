# Dockerfile

# Pull base image
FROM python:3.7.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project and install dependencies
COPY . /code/
RUN pip install -r requirements.txt
