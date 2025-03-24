FROM python:3.9-slim-buster

WORKDIR /app

# Install system dependencies needed to build Python packages like psutil
RUN apt-get update && apt-get install -y gcc python3-dev

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables for Flask
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["flask", "run"]
