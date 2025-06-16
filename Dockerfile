# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only required files
COPY . .

# Install Flask
RUN pip install flask

# Expose the Flask port
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
