FROM python:3.8-slim-buster

ADD . .

ENV FLASK_APP=app.py

RUN python init_db.py

RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0"]