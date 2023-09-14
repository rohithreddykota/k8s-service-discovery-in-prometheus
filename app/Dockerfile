FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install
CMD ["python", "app/server.py"]
