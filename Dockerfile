FROM python:3.10.6

WORKDIR /code

COPY ./package.txt /code/package.txt

RUN pip install --no-cache-dir --upgrade -r /code/package.txt

COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=80" ]