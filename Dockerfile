FROM python:3.12

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY . .

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh

RUN chmod +x /usr/local/bin/wait-for-it.sh

EXPOSE 8000

RUN poetry install

CMD python manage.py runserver 0.0.0.0:8000