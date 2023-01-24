FROM python:3.10.8-alpine

# Set work directory
WORKDIR /src

# Set env variables
# If this is set to a non-empty string, Python won’t try to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1

# Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED 1

# install dev dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


EXPOSE 8000

# Copy project
COPY src /src

CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0"]
