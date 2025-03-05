

# Use an official Python runtime as the base image 
#will change in prod
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/ /app

# Install dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on (5000)
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
