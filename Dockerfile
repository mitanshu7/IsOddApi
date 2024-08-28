# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (our Flask app) into the container at /app
COPY . /app

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Flask and other dependencies
RUN pip3 install -r requirements.txt

# Make port 5010 available for the app
EXPOSE 5010


# Run the command to start the Flask app
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5010", "app:app"]
