  
FROM python:3.8

COPY . .

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080


CMD ["python", "app.py"]