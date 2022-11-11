FROM python:3.10
ENV PYTHONPATH "${PYTHONPATH}:/app"
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt