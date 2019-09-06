FROM python:3.6-alpine
RUN apk update && apk upgrade
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]

