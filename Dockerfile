
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

EXPOSE 5000


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .


CMD ["python", "app.py"]