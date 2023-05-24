FROM python:3.11.3-alpine

RUN apk update && apk add iputils

WORKDIR /app

COPY app2.py /app/app2.py

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "app2.py"]