# Use an official Python runtime as the base image 
# Change in production as needed
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app/ /app
COPY templates/ /app/templates

# Copy the requirements.txt (adjust the path if it's in the root)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on (5000)
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
