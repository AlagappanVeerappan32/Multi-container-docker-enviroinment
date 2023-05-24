FROM python:3.11.3-alpine

RUN apk update && apk add iputils

WORKDIR /app

COPY app1.py /app/app1.py

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000

CMD ["python3", "app1.py"]
