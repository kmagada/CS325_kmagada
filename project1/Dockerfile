FROM python:3.10-slim

WORKDIR /app


# Copy the requirements file inside of the req folder first to leverage Docker's layer caching
# This step only re-runs if requirements.txt changes.
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .