FROM python:3.9

EXPOSE 80

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
