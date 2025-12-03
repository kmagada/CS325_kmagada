FROM python:3.10-slim

WORKDIR /app

# Install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Run tests
CMD ["pytest", "-v"]
