FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY project1/ .

# Run tests
CMD ["pytest", "-v"]
