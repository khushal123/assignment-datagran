FROM python:3.9

WORKDIR /src
COPY . ./src
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_ENV=development 
CMD [ "python3", "app.py" ]