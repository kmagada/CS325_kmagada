    FROM python:3.9-slim-buster
    WORKDIR /app
    COPY hello.py .
    CMD ["python", "hello.py"]