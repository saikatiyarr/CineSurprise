
FROM python:3.9-buster


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=app.py  


EXPOSE 5000

CMD ["python", "-m", "flask", "run"]

