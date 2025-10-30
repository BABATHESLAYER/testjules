# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY threat_analyzer/ ./threat_analyzer/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r threat_analyzer/requirements.txt

# Download the spaCy model
RUN python3 -m spacy download en_core_web_sm

# Train the machine learning model
RUN python3 threat_analyzer/model.py

# Set environment variables for Flask
ENV FLASK_APP=threat_analyzer.app
ENV PYTHONPATH=.

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
