# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y curl

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Ensure Ollama is in PATH
ENV PATH="/root/.ollama/bin:$PATH"

# Copy the application code into the container
COPY app/ /app
COPY app/templates/ /app/templates

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on (5000)
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
