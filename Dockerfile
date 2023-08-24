# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Create a simple Python script
RUN echo "print('Hello, World! v4')" > app.py

# Define the command to run when the container starts
CMD ["python", "app.py"]
