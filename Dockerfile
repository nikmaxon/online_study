FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install —no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]