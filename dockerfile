# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install spaCy and download the English model
RUN pip install spacy==3.0.0 && \
    python -m spacy download en_core_web_md


# Run the Python script when the container launches
CMD ["python", "watch_next.py"]
