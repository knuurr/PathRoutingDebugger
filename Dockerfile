# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the main.py file from the host to the container
COPY main.py .

# Set the entrypoint command to run the main.py file
CMD ["python", "main.py"]