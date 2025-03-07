FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "streamlit", "run", "./app.py", "--server.port", "8080", "--server.address", "0.0.0.0" ]