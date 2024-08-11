# Flask Application with Docker

This repository contains a Flask application that has been dockerized for easy deployment and consistency across different environments.

## Features

1. **Data Retrieval Endpoint**: `/fetch-data` - Simulates fetching data from an external service.
2. **Data Processing Endpoint**: `/process-data` - Processes the fetched data by converting names to uppercase and summing values.
3. **Data Storage Endpoint**: `/get-processed-data` - Returns the processed data stored in memory.

## Setup and Run

### Prerequisites

- Docker (Ensure Docker is installed and running on your machine)

### Building the Docker Image

1. Navigate to the directory containing the `Dockerfile`:
   ```bash
   cd /path/to/flask_app

2. Build the Docker image
   ```bash
   docker build -t flask_app .

3. Run the Docker container
   ```bash
   docker run -p 5000:5000 flask_app
