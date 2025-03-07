FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . /app/

EXPOSE 8080

CMD [ "streamlit", "run", "./app.py" ]