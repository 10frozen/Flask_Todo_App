# Use official Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your app source code
COPY . .

# Expose port 5000 for the app
EXPOSE 5000

# Run gunicorn server on container start
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
