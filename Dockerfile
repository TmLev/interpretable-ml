# pull official base image and pipenv
FROM python
RUN pip install pipenv

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /app

# install dependencies using cache for faster build
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy

# copy everything else
ADD . .

# run server
CMD ["python", "app.py"]
