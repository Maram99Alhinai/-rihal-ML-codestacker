# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create required directories
RUN mkdir -p Dashboard/uploads
RUN mkdir -p Models


# Set environment variables
ENV FLASK_APP=Dashboard/app.py
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 5000

# Change to the Dashboard directory before running
WORKDIR /app/Dashboard

# Command to run the application
CMD ["python", "app.py"]